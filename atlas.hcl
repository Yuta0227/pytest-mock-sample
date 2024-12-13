atlas {
  env = "local"
}

env "local" {
  url = "mysql://root:password@mysql:3306/mock_db"
}

migration {
  dir = "file://migrations"
}