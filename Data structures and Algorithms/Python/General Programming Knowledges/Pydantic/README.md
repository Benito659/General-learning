## Pydantic
Pydantic is a fast and popular Python library used for data validation and settings management. It enforces runtime data types using standard Python type hints, ensuring incoming data matches your expected structure before your application processes it. 

### Problem It Solve
- Lack of static typing in declaration of variable
- A variable can be override by a different type value
```python
    x = 10
    x = "v"
```
- As the app get bigger it become harder to keep track of evry variabl type
- It is also difficult to work with functions where the types aren't obvious
- It allow you to accidently create object with invalid values type
```python
    alice = Person("Alice",24)
    alice = Person("Alice","24")

``` 
- the error will occure only when we will try to use the age
- we can use also @dataclass and type hinting
```python
    @dataclass
    class Person:
        name: str
        age: int
```

### Benefits of Pydantics
- IDE Types Hints
- Data Validation
- JSON Validation
- Fail fast on bad data
- Detects error in Apis

### Installation
```bash
    pip install pydantic
```

### Verify Pydantic is Installed
```bash
    pip show pydantic
```
### Create a pydantic Model
```python
    from pydantic import BaseModel
    class User(BaseModel):
        name:str
        email:str
        account_id:int
```
- we can create an isntance like this :
```python
    user = User(
        name="jack",
        email="jack@pixegami.io",
        account_id=1234
    )
    # can be useful when your data already exists
    user data= {
        "name":"jack",
        "email":"jack@pixegami.io",
        "account":1234
    }
    user = User(**user_data)
```
- Ide can guess the types and variables 
- If we try to create a user with wrong type of data , we will get error
- We  import special data types that verify some data like email or other: EmailStr
```python
    from pydantic import BaseModel, EmailStr
    class User(BaseModel):
        name:str
        email:EmailStr
        account:int
```
- we can use custom validator

### Special Data Types Validator
- EmailStr,Field, SecretStr, ValidationError
- Field function have some couple option 
- we an add some exemle of what are valid
- we can also provide a description
- frozen allow you to only set and not change afterward
- you can also declare an IntFlag class as a custom python validaor


### Custom Validation
- we can add custom validation logic to our model
- for exemple lets say we must ensure account_id is a positive numbers
```python
    from pydantic import BaseModel, EmailStr
    class User(BaseModel):
        name:str
        email:EmailStr
        account_id:int

        @validator("account_id")
        def validate_account_id(cls, value):
            if value <=0 :
                raise ValueError(f"account_id must be positive : {value}")
            return value
```

### JSON Serialization
- Pydantic make it easy to convert Pydantic model to or from Json
- To convert pydantic model to Json , you can call the Json method on the model instance
- This will return a json string of the representation
```python
    user_json_str=user.json()
    print(user_json_str)
```
- we can get a plain python dictionnary
```python
    user_json_obj= user.dict()
```

-  if you have a json string that you want to convert to a pydantic model, you can use parse_raw
```python
    json_str= '{"name":"jack", "email":"jack@pixegami.io", "account_id":1234}'
    user = User.parse_raw(json_str)
```


### Python native capabilities
```python
    x: int = 0
    y: str = "hello"
```
```python
    from dataclass import dataclass

    @dataclass
    class User:
        name: str
        email: str
        account_id: str
        
```
- dataclass are built in while you install pydantic
- but dataclass dont do datavalidation and data validation



### Strict mode, relax mode
- pour preciser que pydantic doit utiliser le mode strict on utilise la classe **ConfigDict()**
```python
    from datetime import datetime
    from pydantic import BaseModel, ConfigDict

    class User(BaseModel):
        id: str
        name: str
        email: str
        adress: str
        date_naissance: datetime

        model_config:ConfigDict(strict=True)
```
- en relax mode il essaie de convertir la valeur dans le type definit dans le schema
- lorsqu'on definit les champs dans pydantic ,on doit tout definir quand on creer un objet, si on veut pouvoir ne pas creer une variable on doit la definir comme optionnel et la definir par defaut a none
```python
    from datetime import datetime
    from typing import Optinal
    from pydantic import BaseModel, ConfigDict

    class User(BaseModel):
        id: str
        name: str
        email: str
        adress: Optional[str] = None
        date_naissance: datetime 
        age: int

        model_config:ConfigDict(strict=True)

    try :
        user = User(
            id= "001",
            name= "John",
            email="john@mail.com",
            adress="12 Street Avenue",
            date_naissance=datetime(2000,5,26),
            age=25
        )
        print(user)
    except Exception as e:
        print("Erreur : ",e)
```


### Field validator
- le field validator permet de verifier qu'un champ respecte bien une valeur
- Nous allon implementer un field validator pour valider le champs email
```python
    import re
    from typing import Optional
    from datetime import datetime
    from pydantic import BaseModel, ConfigDict, field_validator, ValidationError

    class User(BaseModel):
        id: str
        name: str
        email: str
        adress: Optional[str]
        date_naissance: datetime
        age: int

        model_config: ConfigDict(strict=True)

        @field_validator("email")
        def validate_email(cls, input_email):
            pattern = r"^[a-z]+@[a-z]+.[a-z]{2,}"
            if re.match(pattern, input_email) is None:
                raise ValisationError("Le champ email est incorect")
            else :
                return input_email

    try :
        user = User(
            name="john",
            email="john@mail.com",
            adress="12 street avenue",
            date_naissance=datetime(2000, 4, 26),
            age=29

        )   

    except Exception as e:
        print("Erreur : ",e)

``` 
- si on veut clairement voir l'erreur de validation  il faut capturer l'exeption ValidationError


### Model Validator
- le model validator est utiliser quand on veut verifier la coherence entre les champs d'un model pydantic
- on n'a pas besoin de specifier les champs concerner car le model validator de base s'applique a tout les champs de la classe
- le mode ici definit si le model validator doit s'appliquer avent l'instanciation de la classe
- le mode after definit que le model doit s'apliquer apres l'instantiation de la classe
- si on precise after , pydantic va contruire la classe avec tout les champs avent de verifier la coherance des données
```python
    import re
    from typing import Optional
    from datetime import datetime
    from pydantic import BaseModel, ConfigDict, field_validator, ValidationError, model_validator

    class User(BaseModel):
        id: str
        name: str
        email: str
        adress: Optional[str]
        date_naissance: datetime
        age: int

        model_config: ConfigDict(strict=True)

        @field_validator("email")
        def validate_email(cls, input_email):
            pattern = r"^[a-z]+@[a-z]+.[a-z]{2,}"
            if re.match(pattern, input_email) is None:
                raise ValisationError("Le champ email est incorect")
            else :
                return input_email*
        
        @model_validator()
        def validate_email(cls, input_user):
            today= datetime.now()
            year_of_birth= user_input.date_naissance.year
            actual_year= today.year
            if actual_year - year_of_birth != input_user.age:
                raise ValidationError("la date de naissance ne correspond pas a l'age")
            else : 
                return input_user

    try :
        user = User(
            name="john",
            email="john@mail.com",
            adress="12 street avenue",
            date_naissance=datetime(2000, 4, 26),
            age=29

        )   

    except Exception as e:
        print("Erreur : ",e)

```


### Serialisaton and deserialisation
- La sérialisation est le fait de transformer un objet ou des données complexes en une suite de caractères ou de chiffres
- model_dumps permet de transformer un model en dictionnaire, 
- on peut inclure et exclure des champs
```python
    import json
    import re
    from typing import Optional
    from datetime import datetime
    from pydantic import BaseModel, ConfigDict, field_validator, ValidationError, model_validator

    class User(BaseModel):
        id: str
        name: str
        email: str
        adress: Optional[str]
        date_naissance: datetime
        age: int

        model_config: ConfigDict(strict=True)

        @field_validator("email")
        def validate_email(cls, input_email):
            pattern = r"^[a-z]+@[a-z]+.[a-z]{2,}"
            if re.match(pattern, input_email) is None:
                raise ValisationError("Le champ email est incorect")
            else :
                return input_email*
        
        @model_validator()
        def validate_email(cls, input_user):
            today= datetime.now()
            year_of_birth= user_input.date_naissance.year
            actual_year= today.year
            if actual_year - year_of_birth != input_user.age:
                raise ValidationError("la date de naissance ne correspond pas a l'age")
            else : 
                return input_user

    try :
        user = User(
            name="john",
            email="john@mail.com",
            adress="12 street avenue",
            date_naissance=datetime(2000, 4, 26),
            age=29

        )   
        with open("user.json", "w") as file :
            json.dumps(user.model_dumps(mode=json, exclude_none=True), file) 
            file.closed()

        with open("new_user.json","r") as file :
            data = json.loads(file)
            new_user = User(**data)
    except Exception as e:
        print("Erreur : ",e)

```


### Update Validator
- if you use mode before , you have to define @classmethod in the valideror,
- the function will execute at a class level before instanciation
- if you use after mode, no need to use @classmethod and the method will be an isntance(object )  method
