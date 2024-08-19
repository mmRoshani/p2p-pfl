#
# This file is part of the federated_learning_p2p (p2pfl & p2p-pfl) distribution (see https:#github.com/pguijas/federated_learning_p2p & https:#github.com/mmRoshani/p2p-pfl).
# Copyright (c) 2022 Pedro Guijas Bravo & MohammadMojtabaRoshani.
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

"""Heartbeat command."""

from typing import Optional

from interfaces.command import Command
from p2pfl.communication.heartbeater import Heartbeater, HEARTBEATER_CMD_NAME


class HeartbeatCommand(Command):
    """Heartbeat command."""

    def __init__(self, heartbeat: Heartbeater) -> None:
        """Initialize the command."""
        self.__heartbeat = heartbeat

    @staticmethod
    def get_name() -> str:
        """Get the command name."""
        return HEARTBEATER_CMD_NAME

    def execute(
        self, source: str, round: int, time: Optional[str] = None, **kwargs
    ) -> None:
        """
        Execute the command.

        Args:
            source: The source of the command.
            round: The round of the command.
            time: The time of the command.
            **kwargs: The command arguments.

        """
        if time is None:
            raise ValueError("Time is required")
        self.__heartbeat.beat(source, time=float(time))
