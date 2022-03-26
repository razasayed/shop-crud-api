# Project Description

This is a REST API for managing Products and Variants.

# Tech Stack

1. [Flask RESTful](https://flask-restful.readthedocs.io/en/latest/).

2. Gunicorn WSGI server to run the flask application.

3. SQLAlchemy ORM (Object Relational Mapper).

4. Database: MySQL.

5. Docker and Docker Compose for containerizing the app.

6. Postman for testing the API's.

There are two docker containers orchestrated using docker-compose, `api` which runs the Flask application and `db` which runs the MySQL database.

The data in the `db` container is persisted using a docker volume so that it can be recovered even when the containers are removed and recreated.

# Dependencies

This project was developed on a Mac running MacOS Monterey v12.1. However the only dependencies for running this project are as follows:

1. Docker Desktop (https://www.docker.com/products/docker-desktop/)

2. Postman

# Database Design and Project Structure

We have the following four models defined in the `models` directory. Each is associated with a corresponding resource in the `resources` directory.

1. ProductModel (Resource: Product)

2. ProductImageModel (Resource: ProductImage)

3. VariantModel (Resource: Variant)

4. VariantImageModel (Resource: VariantImage)

There is a one to many relationship between the ProductModel and ProductImageModel as one product can have multiple images associated with itself.

There is a one to many relationship between the VariantModel and VariantImageModel as one variant can have multiple images associated with itself.

There is a one to many relationship between the ProductModel and VariantModel as one product can have multiple variants.

The api uses the following 4 tables:

1. `products` table to store the products

2. `product_images` table to store the images for products. Every record is associated with the products table using `product_id` foreign key.

3. `variants` table to store the variants for a particular product. Each record is associated with the products table using `product_id` foreign key.

4. `variant_images` table to store the images for a particular variant. Each record is associated with the variants table using `variant_id` foreign key.


# List Of API's:

We have the following list of 11 REST API's available as per the project requirements:

1. Create a product: `POST /product`

2. Get list of all products: `GET /products`

3. Get a particular product: `GET /product/<product_id>`

4. Update a product: `PUT /product/<product_id>`

5. Create a ProductImage: `POST /product/image`

6. Create a Variant: `POST /variant`

7. Update a Variant: `PUT /variant`

8. Get a list of all variants: `GET /variants`

9. Get a particular variant: `GET /variant/<variant_id>`

10. Get all variants for a particular product: `GET /product/<product_id>/variants`

11. Create a VariantImage: `POST /variant/image`

# Running the project

Run the following command in the project root directory:

`docker-compose up`

To stop running the application run the following command:

`docker-compose stop` 

Run `docker-compose down` if you want to remove all containers as well. The data in the MySQL container will however be persisted in the docker volume.

There is a `postman collection` that i have created which can be imported in Postman to test the API's. The file name is `shop-crud-api.postman_collection.json` located in the project root directory.
