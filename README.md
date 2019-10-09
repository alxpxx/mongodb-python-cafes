# Environment Variables & Hosted Databases

Recently you would have practiced creating a CRUDy RESTful API with your Starship Review app! The part of that exercise that most significantly diverged from a real world REST API was that it used a single `db.json` file as a database. In the real world this would more likely be a SQL database (MySQL, PostSQL), a NoSQL database (MongoDB), or a cache (Redis). As we will be covering SQL and caches later down the track, why not attempt to get started on MongoDB?

[!popular-databases](https://scalegrid.io/blog/wp-content/uploads/2019/02/Most-Popular-Databases-Used-MySQL-MongoDB-PostgreSQL-Redis-Cassandra-Oracle.png)

This will give us time to focus on the DevOps of setting up and connecting to a database, as well as give a viable approach for any hobby applications or side projects you might be thinking of.

### 1. Create a mLab mongoDB database



### 2. Connect to it with a simple script and make changes to it with python. See my example script.

### 3. Make a flask application. It will connect to the database, create some crud.

## Cafes
| Method | Route        | Description                        | Params `application/json`                               |
|--------|--------------|------------------------------------|---------------------------------------------------------|
| GET    | /cafes/      | Return array of all cafes          |                                                         |
| GET    | /cafes/{id}/ | Return cafe of id `id`             |                                                         |
| POST   | /cafes/      | Create cafe                        | `{ "name": string, "coffee": string, "employees": int}` |
| PUT    | /cafes/{id}/ | Update cafe of id with new details | `{ "name": string, "coffee": string, "employees": int}` |
| DELETE | /cafes/{id}/ | Delete cafe of id                  |                                                         |


