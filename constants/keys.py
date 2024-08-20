class Keys:
    """stubs"""

    FILE_NAME_SUFFIX: str = "file_name"

    """engine"""

    ENGINE_RELEASE: str = "engine.release"
    ENGINE_GRPC_TIMEOUT: str = "engine.grpc.timeout"

    """engine.gossip"""
    ENGINE_GOSSIP_PERIOD: str = "engine.gossip.period"
    ENGINE_GOSSIP_TTL: str = "engine.gossip.ttl"
    ENGINE_GOSSIP_MESSAGES_PER_PERIOD: str = "engine.gossip.messages_per_period"
    ENGINE_GOSSIP_AMOUNT_LAST_MESSAGES_SAVED: str = (
        "engine.gossip.amount_last_messages_saved"
    )
    ENGINE_GOSSIP_MODELS_PERIOD: str = "engine.gossip.models_period"
    ENGINE_GOSSIP_MODELS_PER_ROUND: str = "engine.gossip.models_per_round"
    ENGINE_GOSSIP_EXIT_ON_X_EQUAL_ROUNDS: str = "engine.gossip.exit_on_x_equal_rounds"

    "engine.heartbeat"
    ENGINE_HEARTBEAT_PERIOD: str = "engine.heartbeat.period"
    ENGINE_HEARTBEAT_TIMEOUT: str = "engine.heartbeat.timeout"

    "engine.monitoring"
    ENGINE_RESOURCE_MONITORING_PERIOD: str = (
        "engine.monitoring.resource_monitoring_period"
    )
