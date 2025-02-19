"""CHG unique repo_url

Revision ID: a242e0e21f3e
Revises: 592c0d556edf
Create Date: 2021-08-24 13:53:49.356158

"""
from alembic import op
import alembic
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a242e0e21f3e"
down_revision = "592c0d556edf"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("assignment_repo", "repo_url", type_=sa.String(512))
    op.create_unique_constraint(None, "assignment_repo", ["repo_url"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("assignment_repo", "repo_url", type_=sa.TEXT(512))
    op.drop_constraint("repo_url", "assignment_repo", type_="unique")
    # ### end Alembic commands ###
