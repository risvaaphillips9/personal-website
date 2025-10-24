import io


def test_projects_page_renders(client, app_module):
    # Baseline projects should be present from app startup
    resp = client.get("/projects")
    assert resp.status_code == 200
    html = resp.get_data(as_text=True)
    assert "Corporate Programs Management System" in html
    assert "Global Market Entry Strategy" in html


def test_add_project_validation_missing_image(client):
    # Missing image should trigger validation and 400 response
    resp = client.post(
        "/add-project",
        data={
            "title": "No Image Project",
            "description": "Should fail due to missing image",
        },
        content_type="multipart/form-data",
        follow_redirects=False,
    )
    assert resp.status_code == 400


def test_add_project_success(client, app_module):
    # Create a tiny in-memory PNG header to simulate an image upload
    fake_png = io.BytesIO(
        b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR" + b"0" * 64
    )
    fake_png.name = "upload.png"

    resp = client.post(
        "/add-project",
        data={
            "title": "Uploaded Project",
            "description": "Added via test upload",
            "image_file": (fake_png, "upload.png"),
        },
        content_type="multipart/form-data",
        follow_redirects=False,
    )

    # Expect redirect to /projects on success
    assert resp.status_code in (301, 302)

    # Verify new project appears on the projects page
    page = client.get("/projects")
    assert page.status_code == 200
    assert "Uploaded Project" in page.get_data(as_text=True)
