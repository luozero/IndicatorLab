def generate_alpha101_factors(fun_ids, df=None):

    from qaenv import (clickhouse_ip, clickhouse_password, clickhouse_port,
                      clickhouse_user)
    for i in fun_ids:
        
        fun_name = 'alpha101_'+str(i)
        factor_base = alpha101(fun_name, host=clickhouse_ip, port=clickhouse_port, user=clickhouse_user, password=clickhouse_password)
        factor_base.update_to_database(df)
