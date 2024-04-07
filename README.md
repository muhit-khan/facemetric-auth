# Facemetric Authentication

## Overview

This Docker image provides a web-based face authentication server built with Python and Flask. It leverages the DeepFace library for accurate and reliable facial recognition, offering enhanced security features and error handling.

## Features

- **Enhanced Security:**
  - Random folder generation for uploads to prevent unauthorized access.
  - File validation to ensure only authorized image formats (JPG, JPEG, PNG, BMP, GIF) are accepted.
  - Secure file deletion after processing to maintain privacy.
- **Robust Face Comparison:**
  - Utilizes DeepFace's deep learning-based facial recognition for accurate matching.
- **Error Handling:**
  - Graceful exception management during DeepFace operations and file processing.
- **User-Friendly API:**
  - Simple POST endpoint (`/compare`) for face comparisons.
  - Clear request parameters and JSON response format.
  - Comprehensive error handling with informative messages.
- **Development Stack:**
  - Flask: Lightweight web framework for API creation.
  - Werkzeug: WSGI utility toolkit for secure file uploads.
  - DeepFace: Deep learning library for facial recognition.
  - Secrets: Built-in module for generating secure random folder names.
  - OS: Module for file system operations.

## Usage

1. **Visit the DockerHub Repository:** ["https://hub.docker.com/repository/docker/muhitkhan/facemetric-authentication/"](https://hub.docker.com/repository/docker/muhitkhan/facemetric-authentication/)

2. **Pull the Docker image:**

```bash
docker image pull muhitkhan/facemetric-authentication:tagname
```

3. **Run the container:**

```bash
docker run -it -p 5000:5000 muhitkhan/facemetric-authentication:tagname
```

4. **Access the API:**

- Send a POST request to `http://localhost:5000/compare` with the following parameters:
- `reference_image`: The reference image file.
- `live_image`: The live image file for comparison.

## Example Request:

### Using Postman

    1. Open Postman.
    2. Create a new request.
    3. Set the request method to POST.
    4. Enter the API endpoint URL: `http://localhost:5000/compare`  (replace `localhost` with the actual IP address or hostname if the   server is running on a different machine).
    5. Go to the "Body" tab.
    6. Select "form-data" as the body type.
    7. Add two key-value pairs:
        - Key: `reference_image`
        - Vaule: Select "File" from the dropdown and choose reference   image file from your computer.
        - Key: `live_image`
        - Value: Select "File" from the dropdown and choose the live image  file from your computer.
    8. Click "Send" to send the request.

Postman will send the form data request to the API endpoint, and you should receive a JSON response indicating whether the faces in the two images match.

### Using CLI

```
curl -X POST \
http://localhost:5000/compare \
-F reference_image=@reference.jpg \
-F live_image=@live.jpg
```

## Example Response:

```json
{
  "identical": true
}
```

_Note: Make sure your Facemetric Authentication server is running and accessible at the specified URL before sending the request._

## Developer Credit

Developed with love by [MUHIT KHAN](https://linkedin.com/in/muhit-khan)

## Additional Notes

- The Docker image is built for Python 3.10 and includes all necessary dependencies.
- The container exposes port 5000 by default. You can adjust this using the `-p` flag when running the container.
- For more detailed information and usage examples, please refer to the project's documentation or source code.
