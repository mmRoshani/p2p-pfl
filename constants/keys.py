class Keys:
    """stubs"""

    FILE_NAME_SUFFIX: str = "file_name"

    """engine"""

    ENGINE_RELEASE: str = "engine_release"
    ENGINE_GRPC_TIMEOUT: str = "engine_grpc_timeout"
    ENGINE_GRPC_TIMEOUT: str = "engine_grpc_timeout"
    """engine/gossip"""
    ENGINE_GOSSIP_PERIOD: str = "engine_gossip_period"
    ENGINE_GOSSIP_TTL: str = "engine_gossip_ttl"
    ENGINE_GOSSIP_MESSAGES_PER_PERIOD: str = "engine_gossip_messages_per_period"
    ENGINE_GOSSIP_AMOUNT_LAST_MESSAGES_SAVED: str = (
        "engine_gossip_amount_last_messages_saved"
    )
    ENGINE_GOSSIP_MODELS_PERIOD: str = "engine_gossip_models_period"
    ENGINE_GOSSIP_MODELS_PER_ROUND: str = "engine_gossip_models_per_round"
    ENGINE_GOSSIP_EXIT_ON_X_EQUAL_ROUNDS: str = "engine_gossip_exit_on_x_equal_rounds"

    "engine/heartbeat"
    HEARTBEAT_PERIOD: float = "heartbeat_period"
    HEARTBEAT_TIMEOUT: float = "heartbeat_timeout"
