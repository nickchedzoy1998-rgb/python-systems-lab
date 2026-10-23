from collections.abc import Mapping
from types import MappingProxyType


def get_database_port(
        config: Mapping[str, object],
        default: int = 5432,
    ) -> int:

    port = config.get('port')

    if isinstance(port, int) and not isinstance(port, bool): 
        return port

    return default


if __name__ == '__main__':
    # print(get_database_port({"port": 5433}))         # 5433
    # print(get_database_port({"host": "localhost"}))  # 5432
    # print(get_database_port({"port": "5433"}))       # 5432
    # print(get_database_port({"port": True}))         # 5432
    # print(get_database_port({}, default=6000))       # 6000


    config = MappingProxyType({'port': 5433})

    print(get_database_port(config))