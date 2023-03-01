import operation
import repository
import controller
import view


if __name__ == '__main__':
    file = operation.FileOperation('notes.csv')
    repo = repository.Repository(file)
    _controller = controller.Controller(repo)
    _view = view.View(_controller)
    _view.run()
