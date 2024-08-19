#
# This file is part of the federated_learning_p2p (p2pfl & p2p-pfl) distribution (see https:#github.com/pguijas/federated_learning_p2p & https:#github.com/mmRoshani/p2p-pfl).
# Copyright (c) 2024 Pedro Guijas Bravo & MohammadMojtabaRoshani.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http:#www.gnu.org/licenses/>.
#

"""gRPC neighbors."""

import time
from typing import Optional, Tuple

import grpc

from grpc.compiled import node_pb2, node_pb2_grpc
from configs.engine.engine_bootstrap import engine_bootstrap
from configs.self.log.logger_bootstrap import logger_bootstrap
from constants.keys import Keys
from constants.paths import Paths
from helpers.neighbors import Neighbors


class GrpcNeighbors(Neighbors):
    """Implementation of the neighbors for a GRPC communication protocol."""

    engine_config = engine_bootstrap(Paths.ENGINE_CONFIG)
    log = logger_bootstrap(
        instance_name=__name__,
        log_config_file_name=Paths.LOGGER_CONFIG,
    )

    def refresh_or_add(self, addr: str, time: float) -> None:
        """
        Refresh or add a neighbor.

        Args:
            addr: Address of the neighbor.
            time: Time of the last heartbeat.

        """
        # Update if exists
        if addr in self.neis:
            # Update time
            self.neis_lock.acquire()
            self.neis[addr] = (
                self.neis[addr][0],
                self.neis[addr][1],
                time,
            )
            self.neis_lock.release()
        else:
            # Add
            self.add(addr, non_direct=True)

    def connect(
        self, addr: str, non_direct: bool = False, handshake_msg: bool = True
    ) -> Tuple[Optional[grpc.Channel], Optional[node_pb2_grpc.NodeServicesStub], float]:
        """
        Connect to a neighbor.

        Args:
            addr: Address of the neighbor to connect.
            non_direct: If the connection is direct or not.
            handshake_msg: If a handshake message is needed.

        """
        if non_direct:
            return self.__build_non_direct_neighbor(addr)
        else:
            return self.__build_direct_neighbor(addr, handshake_msg)

    def __build_direct_neighbor(
        self, addr: str, handshake_msg: bool
    ) -> Tuple[Optional[grpc.Channel], Optional[node_pb2_grpc.NodeServicesStub], float]:
        try:
            # Create channel and stub
            channel = grpc.insecure_channel(addr)
            stub = node_pb2_grpc.NodeServicesStub(channel)

            if not stub:
                raise Exception(f"Cannot create a stub for {addr}")

            # Handshake
            if handshake_msg:

                engine_grpc_timeout: str = str(
                    self.engine_config.get(Keys.ENGINE_GRPC_TIMEOUT)
                )

                res = stub.handshake(
                    node_pb2.HandShakeRequest(addr=self.self_addr),
                    timeout=engine_grpc_timeout,
                )
                if res.error:
                    self.log.info(self.self_addr, f"Cannot add a neighbor: {res.error}")
                    channel.close()
                    raise Exception(f"Cannot add a neighbor: {res.error}")

            # Add neighbor
            return (channel, stub, time.time())

        except Exception as e:
            self.log.info(self.self_addr, f"Crash while adding a neighbor: {e}")
            # Re-raise exception
            raise e

    def __build_non_direct_neighbor(self, _: str) -> Tuple[None, None, float]:
        return (None, None, time.time())

    def disconnect(self, addr: str, disconnect_msg: bool = True) -> None:
        """
        Disconnect from a neighbor.

        Args:
            addr: Address of the neighbor to disconnect.
            disconnect_msg: If a disconnect message is needed.

        """
        try:
            # If the other node still connected, disconnect
            node_channel, node_stub, _ = self.get(addr)
            if disconnect_msg:
                if node_stub is not None:
                    node_stub.disconnect(node_pb2.HandShakeRequest(addr=self.self_addr))
                # Close channel
                if node_channel is not None:
                    node_channel.close()
        except Exception:
            pass
