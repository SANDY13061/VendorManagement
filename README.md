Vendor Management System
------------------------

This project is a Vendor Management System built using Django and Django REST Framework. It allows you to manage vendor profiles, track purchase orders, and evaluate vendor performance metrics.

Setup Instructions
------------------

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/SANDY13061/VendorManagement.git


2. **Navigate to the Project Directory:**

   ```bash
   cd vendarManagement

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Apply Migrations:**
    ```bash
    python manage.py migrate

5. **Create a Superuser (Optional, for admin access):**
    ```bash
    python manage.py createsuperuser

6. **Run the Development Server:**
    ```bash
    python manage.py runserver

You can access the API at [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/).

## API Endpoints

### Create a new vendor:

- **Endpoint:** POST /api/vendors/
- **Input Parameters:** JSON
  ```json
  {
      "name": "Vendor Name",
      "contact_details": "Contact Information",
      "address": "Vendor Address",
      "vendor_code": "Unique Vendor Code"
  }
- **Example:**
  ```bash
  curl -X POST http://127.0.0.1:8000/api/vendors/ -d '{"name": "Vendor Name", "contact_details": "Contact Information", "address": "Vendor Address", "vendor_code": "Unique Vendor Code"}' -H 'Content-Type: application/json'

### List all vendors:

- **Endpoint:** GET /api/vendors/
- **Example:**
  ```bash
  curl http://127.0.0.1:8000/api/vendors/


### Retrieve details of a specific vendor:

- **Endpoint:** GET /api/vendors/{vendor_id}/
- **Example:**
  ```bash
  curl http://127.0.0.1:8000/api/vendors/1/

### Update a vendor's details:

- **Endpoint:** PUT /api/vendors/{vendor_id}/
- **Input Parameters (same format as POST):**
  ```json
  {
      "name": "Updated Vendor Name",
      "contact_details": "Updated Contact Information",
      "address": "Updated Vendor Address",
      "vendor_code": "Updated Unique Vendor Code"
  }
- **Example:**
  ```bash
  curl -X PUT http://127.0.0.1:8000/api/vendors/1/ -d '{"name": "Updated Vendor Name", "contact_details": "Updated Contact Information", "address": "Updated Vendor Address", "vendor_code": "Updated Unique Vendor Code"}' -H 'Content-Type: application/json'

### Delete a vendor:

- **Endpoint:** DELETE /api/vendors/{vendor_id}/
- **Example:**
  ```bash
  curl -X DELETE http://127.0.0.1:8000/api/vendors/1/
Purchase Order Tracking
[...]

Authentication
The API endpoints are secured with token-based authentication. To access authenticated endpoints, include the token in the Authorization header:

makefile
Copy code
Authorization: Token YOUR_TOKEN_HERE
Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.
 
