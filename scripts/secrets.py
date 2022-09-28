mssql_user = '<user_name>'
mssql_pass = '<user_password>'

server = '<server>'
db = '<database>'
driver = '<driver>'.replace(' ', '+')
connection = 'mssql+pyodbc://{}:{}@{}/{}?driver={}&TrustServerCertificate=Yes'.format(mssql_user,
                                                                                      mssql_pass,
                                                                                      server,
                                                                                      db,
                                                                                      driver)