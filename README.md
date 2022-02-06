
# Pratilipi Backend Assignment




## Run Locally

Clone the project

```bash
  git clone https://github.com/shiyanshirani/Pratilipi-BackendAssignment
```

Go to the project directory

```bash
  cd Pratilipi
```

Build Docker image. (Prerequisite - make)
```bash
  make build
```

Start all the microservices

```bash
  make up
```


## Screenshots

![Architecture Diagram](assets/architecture-diagram.png)


## Testing

To run tests, run the following command

```http
  POST http://127.0.0.1:8000/api/books
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `input_file` | `file` | **csv file**. |



## Documentation
- Swagger documentation
```http
 http://127.0.0.0.1/8000/docs
 http://127.0.0.1/8001/docs
 http://127.0.0.0.1/8002/docs
```
 - [Postman Collection]()
## Acknowledgements
 - [Design with developer empathy](https://apiguide.readthedocs.io/en/latest/principles/empathy.html#:~:text=Design%20with%20developer%20empathy&text=Perhaps%20the%20most%20important%20criteria,will%20remain%20undiscovered%20or%20unrealised)
 - [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
## License

- [MIT](https://choosealicense.com/licenses/mit/)

0
