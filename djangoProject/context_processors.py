from trainer.models import Trainer

def get_all_trainers(request):
    get_trainers = Trainer.objects.all()
    return {'trainers': get_trainers}