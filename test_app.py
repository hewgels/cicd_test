from main import app

def test_home():
  response = app.test_client().get("/")
  print(response.data)
  assert response.status_code == 200
  assert b"Hello" in response.data