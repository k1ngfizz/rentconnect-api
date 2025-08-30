
# RentConnect API

RentConnect is a RESTful API for house rental management, connecting landlords and tenants. Features include property listing CRUD, user authentication, search & filtering, and booking requests.

## Features

- User registration & JWT authentication (landlord or tenant)
- Landlords can create, update, delete their own rental properties
- Tenants can browse, search, and filter listings
- Booking requests (tenants express interest)
- Role-based permissions

## Tech Stack

- Python, Django, Django REST Framework, SimpleJWT, SQLite


## API Endpoints

| Method | Endpoint                | Description                         |
|--------|------------------------ |-------------------------------------|
| POST   | /auth/register/         | Register as tenant or landlord      |
| POST   | /auth/login/            | Login (JWT)                         |
| GET    | /properties/            | List/filter all properties          |
| POST   | /properties/            | Create property (landlord only)     |
| GET    | /properties/<id>/       | View property details               |
| PUT    | /properties/<id>/       | Update property (owner only)        |
| DELETE | /properties/<id>/       | Delete property (owner only)        |
| POST   | /bookings/              | Send booking request (tenant only)  |
| PATCH  | /bookings/<id>/         | Update booking status (landlord)    |

Authentication: JWT `Authorization: Bearer <token>`

## License

MIT
