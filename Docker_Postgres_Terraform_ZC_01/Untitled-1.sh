
docker run -it \
  -e POSTGRES_USER= "root" \
  -e  POSTGRES_PASSWORD= "root" \
  -e  POSTGRES_DB= "ny_taxi" \
  -v c:/workspaces/Sa-lZooCamp2025/Docker_Postgres_Terraform_ZC_01/ny_taxi_db \
  -p 5432:5432 \
  postgres:13

docker run -it \
  -e POSTGRES_USER=root \
  -e POSTGRES_PASSWORD=root \
  -e POSTGRES_DB=ny_taxi \
  -v /c/workspaces/Sa-lZooCamp2025/Docker_Postgres_Terraform_ZC_01/ny_taxi_db:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13

  docker run -it \
  -e POSTGRES_USER=root \
  -e POSTGRES_PASSWORD=root \
  -e POSTGRES_DB=ny_taxi \
  -v /c/workspaces/Sa-lZooCamp2025/Docker_Postgres_Terraform_ZC_01/db_ny_taxi:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13

  pgcli -h localhost -p 5432 -u root -d ny_taxi

  docker run -it \

  docker pull dpage/pgadmin4

docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  dpage:/pgadmin4

#network
  docker network create pg-network

  docker run -it \
  -e POSTGRES_USER=root \
  -e POSTGRES_PASSWORD=root \
  -e POSTGRES_DB=ny_taxi \
  -v /c/workspaces/Sa-lZooCamp2025/Docker_Postgres_Terraform_ZC_01/db_ny_taxi:/var/lib/postgresql/data \
  -p 5432:5432 \
  --network=pg-network \
  --name pgadmin
  dpage/pgadmin4

 docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  --network=pg-network \
  --name pgadmin-4 \
  dpage/pgadmin4