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

4. **Apply Migrate:**
    ```bash
    python manage.py migrate

5. **Apply Migrations:**
    ```bash
    python manage.py makemigrations

6. **Create a Superuser (Optional, for admin access):**
    ```bash
    python manage.py createsuperuser
7. **Run the Development Server:**
    ```bash
    python manage.py runserver

You can access the API at [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/).

## API Endpoints

## Authentication

The API endpoints are secured with token-based authentication. To access authenticated endpoints, include the token in the Authorization header:
![Project Logo](C:\VendorManagement\vendarManagement\AUTH.png)


### Create a new Token:

- **Endpoint:** POST api/register-token/
- **Input Parameters:** JSON
  ```json
  {
      "name": "Your Name",
      "password": "Your Password"
  }
- **Example:**
  ```bash
  curl -X POST http://127.0.0.1:8000/api/vendors/ -d '{"name": "Your Name", "password": "Your Password"' -H 'Content-Type: application/json'

### Get Your Token:

- **Endpoint:** POST api/get-auth-token/
- **Input Parameters:** JSON
  ```json
  {
      "name": "Your Name",
      "password": "Your Password"
  }
- **Example:**
  ```bash
  curl -X POST http://127.0.0.1:8000/api/vendors/ -d '{"name": "Your Name", "password": "Your Password"' -H 'Content-Type: application/json'



## Vendor

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

<!-- # Purchase Order Tracking API -->

<!-- You can access the API at [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/). -->

## Purchase Order

### Create a new purchase order:

- **Endpoint:** POST /api/purchase_orders/
- **Input Parameters:** JSON
  ```json
  {
        "po_number": "Purchase Order ID",
        "order_date": "Order Date With Time",
        "delivery_date": "Delivery Date With Time",
        "items": "List Of Items In JSON Formate",
        "quantity": "Quantity in Number",
        "status": "Status of the Work",
        "quality_rating": "Quality Rating Of The Items",
        "issue_date": "Issue Date With Time",
        "acknowledgment_date": "Acknowledgment Date With Time",
        "vendor": "Vendor Id "
    }
- **Example:**
  ```bash
  curl -X POST http://127.0.0.1:8000/api/purchase_orders/ -d '{"po_number": "10","order_date":"2024-04-01T15:21:12Z","delivery_date": "2024-04-27T15:21:16Z","items": {"item1": "django"}, "quantity": 5,"status": "completed","quality_rating": 5.0,"issue_date": "2024-04-03T15:22:27Z","acknowledgment_date": "2024-04-27T15:22:38Z","vendor": 1}' -H 'Content-Type: application/json'

### List all Purchase Order:

- **Endpoint:** GET /api/purchase_orders/
- **Example:**
  ```bash
  curl http://127.0.0.1:8000/api/purchase_orders/


### Retrieve details of a specific Purchase Order:

- **Endpoint:** GET /api/purchase_orders/{purchase_orders_id}/
- **Example:**
  ```bash
  curl http://127.0.0.1:8000/api/purchase_orders/1/

### Update a purchase order's details:

- **Endpoint:** PUT /api/purchase_orders/{purchase_orders_id}/
- **Input Parameters (same format as POST):**
  ```json
  {
        "po_number": "Purchase Order ID",
        "order_date": "Order Date With Time",
        "delivery_date": "Delivery Date With Time",
        "items": "List Of Items In JSON Formate",
        "quantity": "Quantity in Number",
        "status": "Status of the Work",
        "quality_rating": "Quality Rating Of The Items",
        "issue_date": "Issue Date With Time",
        "acknowledgment_date": "Acknowledgment Date With Time",
        "vendor": "Vendor Id "
    }
- **Example:**
  ```bash
  curl -X POST http://127.0.0.1:8000/api/purchase_orders/ -d '{"po_number": "10","order_date":"2024-04-01T15:21:12Z","delivery_date": "2024-04-27T15:21:16Z","items": {"item1": "updatedjango"}, "quantity": 7,"status": "completed","quality_rating": 5.0,"issue_date": "2024-04-03T15:22:27Z","acknowledgment_date": "2024-04-27T15:22:38Z","vendor": 3}' -H 'Content-Type: application/json'

### Delete a purchase order:

- **Endpoint:** DELETE /api/purchase_orders/{purchase_orders_id}/
- **Example:**
  ```bash
  curl -X DELETE http://127.0.0.1:8000/api/purchase_orders/1/





## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.
 
