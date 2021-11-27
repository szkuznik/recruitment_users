# recruitment_users
Recruitment project I created for TRAVELIST

# Run project
- Installation:
`docker-compose up --build`
- List of users: http://localhost:8000/api/users/users/
- Modify user budget http://localhost:8000/api/users/users/{id}/modify_points/

# ToDo
- Add possibility to update users through csv importer
- Add translations to BalanceHistory types
- Instead of skipping header we could use it to map fields to columns
- Add authentication and permissions to API
- Importer does not import ID
- Add unit tests
- Add Admin Panel
# Potential problems
- When we import users if we first import referred user and then referer, he won't get any points.
Potential fix: while reading csv store list of all referrers, and award them points after reading is finished.
- User balance can be negative
