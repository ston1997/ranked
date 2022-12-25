# SRS:
Develop a RESTful web service to obtain ranked courses information.

The following information about the course should be stored in the database:
1. Title
2. Overview
3. Rating (min value - 1, max value - 5)
4. Price

Create API endpoints to get a list of courses and detailed information about a particular courses.

The endpoint with collection of courses should return the following:
1. Title
2. Rating
3. Price
Users should be able to order courses by rating, title (multiply by ids) and search by title. 
Default ordering by rating (desc).

The endpoint with detailed information should return the following:
1. Title
2. Overview
3. Rating
4. Price