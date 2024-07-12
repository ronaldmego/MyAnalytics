library(RRedshiftSQL)

# Establish the connection
con <- dbConnect(RedshiftSQL(),
                drv = "PostgreSQL",
                user=Sys.getenv("USER_NAME"),
                password =Sys.getenv("PASSWORD"),
                host=Sys.getenv("HOST"), 
                dbname=Sys.getenv("DBNAME"), 
                port = Sys.getenv("PORT"))

# Create a query
query <- "SELECT 'PY' AS COUNTRY, 'INFO_DYN_PY_CLIENT' AS FUENTE, MAX(date(EXTRACTION_DATE))
FROM INFORMATION_DELIVERY_PROD.MFS_LENDING.INFO_DYN_PY_CLIENT"

# Send the query to the database
res <- dbSendQuery(con, query)

# Fetch the results as a dataframe
df <- dbFetch(res)

# Print the resulting dataframe
print(df)

# Don't forget to close the connection when you're done
dbDisconnect(con)