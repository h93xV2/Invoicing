from datetime import datetime

from model_validation.field import StringField, FloatField, Field, ForeignKeyField, \
    DateField, IntegerField
from model_validation.validations import IsRequired, IsString
from models.base_model import BaseModel
from models.staff_model import StaffModel
from models.status_model import StatusModel
from relationships.base_relationship import BaseRelationship
from repository.staff_repository import StaffRepository
from repository.status_repository import StatusRepository


class JobModel(BaseModel):
    title = StringField([IsRequired()])
    description = StringField([IsRequired()])
    estimated_time = FloatField([IsRequired()])
    deadline = DateField([IsRequired()])
    assigned_to = ForeignKeyField(
        BaseRelationship('Staff', StaffRepository, StaffModel)
    )
    status_id = ForeignKeyField(
        BaseRelationship('Status', StatusRepository, StatusModel)
    )
    project_id = IntegerField([IsRequired()], initial_value=0, updatable=False)
    created_at = Field([IsString()], initial_value=datetime.now().strftime("%Y-%m-%d %H:%M"), updatable=False)
