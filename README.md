# Online courses shop

Shop with online courses developing in awesome (xd) Prestashop framework.
## Installation

### SSL
~~In order to run on https connection you must generate CA and certificate and add CA certificate to trusted CAs in your browser.
To generate CA and certificate for localhost signed by CA run:~~
```bash
sudo ./certificate.sh
```
~~You only need to do this once.~~
TO BE DONE

### Permissions
All files have to be owned by `www-data`. In order to do that, run command in BE-project folder:
```bash 
sudo chown -R www-data:www-data .
```

### Running container
Use docker-compose to run the container:

```bash
docker-compose up
```
**Note**: You can add flag `--build` to rebuild already created images on your OS. Without it not all changes may be reflected.

To shut down container use:

```bash
docker-compose down
```

## Accessing admin page
To go to admin page visit `https://localhost/admin1` and fill:
```
email: admin@admin.com
password: 12345678
```

## File structure
Prestashop source and configuration files inside the container are replaced by those in `src/` folder.

At start, db dump from `db/` folder is applied to MySQL container.  

## Changing db dump
If there are any changes applied to db you should contain a proper SQL dump in your PR. For example all configurations changed in admin panel are saved in databse. In order to get sql dump from container run:

```bash
docker exec be-project_ps1_db_1 /usr/bin/mysqldump -u root --password=admin ps > /tmp/dump.sql
```
Then replace `db/dump.sql` with `/tmp/dump.sql`

## Contributing
Please open a pull request to contribute any changes. Do not commit to main! 

## License
[MIT](https://choosealicense.com/licenses/mit/)
