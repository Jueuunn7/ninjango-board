# ninjango-board
ninja-extra를 사용해서 DRF의 여러 단점과 ninja에 단점을 줄여 CRUD 게시판을 만듭니다. https://jueuunn7.tistory.com/28   

## 설명

### controller(view) 클래스화, DI
ninja에선 함수로 컨트롤러를 만들었지만 ninja-extra로 class로 개선     
DRF, ninja에선 안되는 DI를 계층별 적용하여 사용
```py
@api_controller('/board')
class BoardController:
    @inject
    def __init__(self, board_service: BoardService):
        self.board_service = board_service
```


### 메서드 체이닝과 데코레이터로 데이터 검증 단순화
반복되는 `if not data` 구문을 데코레이터를 사용해서 단순화
```py
class Repository:
    def notfound(func):
        def wrapper(*args, **kwargs):
            return DoesNotExist(func(*args, **kwargs))

        class DoesNotExist:
            def __init__(self, data):
                self.data = data

            def NotFound(self, exception_class):
                if self.data is None:
                    raise exception_class
                return self.data
            
        return wrapper

@Repository.notfound
def find_by_id(self, id) -> Board:
    return Board.objects.filter(id=id).first()

def get_board_by_id(self, id):
    return self.board_repository.find_by_id(id)\
        .NotFound(BoardNotFoundException)
```
