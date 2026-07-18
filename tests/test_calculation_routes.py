def test_create_calculation(client):
    response = client.post(
        "/calculations",
        json={
            "a": 10,
            "b": 5,
            "type": "Add",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["a"] == 10
    assert data["b"] == 5
    assert data["type"] == "Add"
    assert data["result"] == 15
    assert "id" in data


def test_browse_calculations(client):
    client.post(
        "/calculations",
        json={
            "a": 10,
            "b": 5,
            "type": "Add",
        },
    )

    client.post(
        "/calculations",
        json={
            "a": 8,
            "b": 2,
            "type": "Divide",
        },
    )

    response = client.get("/calculations")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 2
    assert data[0]["result"] == 15
    assert data[1]["result"] == 4


def test_read_calculation(client):
    create_response = client.post(
        "/calculations",
        json={
            "a": 20,
            "b": 4,
            "type": "Divide",
        },
    )

    calculation_id = create_response.json()["id"]

    response = client.get(
        f"/calculations/{calculation_id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == calculation_id
    assert data["a"] == 20
    assert data["b"] == 4
    assert data["type"] == "Divide"
    assert data["result"] == 5


def test_update_calculation(client):
    create_response = client.post(
        "/calculations",
        json={
            "a": 10,
            "b": 5,
            "type": "Add",
        },
    )

    calculation_id = create_response.json()["id"]

    response = client.put(
        f"/calculations/{calculation_id}",
        json={
            "a": 10,
            "b": 5,
            "type": "Multiply",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == calculation_id
    assert data["type"] == "Multiply"
    assert data["result"] == 50


def test_delete_calculation(client):
    create_response = client.post(
        "/calculations",
        json={
            "a": 9,
            "b": 3,
            "type": "Sub",
        },
    )

    calculation_id = create_response.json()["id"]

    delete_response = client.delete(
        f"/calculations/{calculation_id}"
    )

    assert delete_response.status_code == 204

    get_response = client.get(
        f"/calculations/{calculation_id}"
    )

    assert get_response.status_code == 404
    assert get_response.json()["detail"] == "Calculation not found."


def test_create_division_by_zero(client):
    response = client.post(
        "/calculations",
        json={
            "a": 10,
            "b": 0,
            "type": "Divide",
        },
    )

    assert response.status_code == 422


def test_create_invalid_calculation_type(client):
    response = client.post(
        "/calculations",
        json={
            "a": 10,
            "b": 5,
            "type": "Power",
        },
    )

    assert response.status_code == 422


def test_read_missing_calculation(client):
    response = client.get("/calculations/99999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Calculation not found."


def test_update_missing_calculation(client):
    response = client.put(
        "/calculations/99999",
        json={
            "a": 10,
            "b": 5,
            "type": "Add",
        },
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Calculation not found."


def test_delete_missing_calculation(client):
    response = client.delete("/calculations/99999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Calculation not found."