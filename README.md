# migration in atlas container
1. atlas migrate apply --url mysql://root:password@mysql:3306/mock_db

# setup for development
1. docker compose up --build
2. reopen in container
3. run debugger
4. access localhost:15000/docs
5. try /posts/{post_id} API


# pytest preparations
1. docker compose exec atlas bash
2. atlas migrate apply --url mysql://root:password@mysql_test:3306/test_mock_db
3. exit
4. docker compose exec api bash
2. pytest -vvv --cov=app/ --cov-report=html -s ./tests > output.txt
