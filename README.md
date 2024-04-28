Vendor Management System
------------------------

This project is a Vendor Management System built using Django and Django REST Framework. It allows you to manage vendor profiles, track purchase orders, and evaluate vendor performance metrics.

Setup Instructions
------------------

**Clone the Repository:**

   ```bash
   git clone https://github.com/SANDY13061/VendorManagement.git

Navigate to the Project Directory:
------------------
bash
Copy code
cd vendor-management-system
Install Dependencies:
bash
Copy code
pip install -r requirements.txt
Apply Migrations:
bash
Copy code
python manage.py migrate
Create a Superuser (Optional, for admin access):
bash
Copy code
python manage.py createsuperuser
Run the Development Server:
bash
Copy code
python manage.py runserver
Access the API:You can access the API at http://127.0.0.1:8000/api/.
API Endpoints
Vendor Profile Management
Create a new vendor:
Endpoint: POST /api/vendors/
Input Parameters:
json
Copy code
{
    "name": "Vendor Name",
    "contact_details": "Contact Information",
    "address": "Vendor Address",
    "vendor_code": "Unique Vendor Code"
}
Example:
bash
Copy code
curl -X POST http://127.0.0.1:8000/api/vendors/ -d '{"name": "Vendor Name", "contact_details": "Contact Information", "address": "Vendor Address", "vendor_code": "Unique Vendor Code"}' -H 'Content-Type: application/json'
List all vendors:
Endpoint: GET /api/vendors/
Example:
bash
Copy code
curl http://127.0.0.1:8000/api/vendors/
Retrieve details of a specific vendor:
Endpoint: GET /api/vendors/{vendor_id}/
Example:
bash
Copy code
curl http://127.0.0.1:8000/api/vendors/1/
Update a vendor's details:
Endpoint: PUT /api/vendors/{vendor_id}/
Input Parameters (same format as POST)
Example:
bash
Copy code
curl -X PUT http://127.0.0.1:8000/api/vendors/1/ -d '{"name": "Updated Vendor Name", "contact_details": "Updated Contact Information", "address": "Updated Vendor Address", "vendor_code": "Updated Unique Vendor Code"}' -H 'Content-Type: application/json'
Delete a vendor:
Endpoint: DELETE /api/vendors/{vendor_id}/
Example:
bash
Copy code
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
 
