"""CHG repo url optional

Revision ID: 2f5a27ffe4ea
Revises: 49d73a536492
Create Date: 2021-08-09 12:20:47.472452

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "2f5a27ffe4ea"
down_revision = "49d73a536492"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "theia_session",
        "repo_url",
        existing_type=mysql.VARCHAR(collation="utf8mb4_unicode_ci", length=128),
        nullable=True,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "theia_session",
        "repo_url",
        existing_type=mysql.VARCHAR(collation="utf8mb4_unicode_ci", length=128),
        nullable=False,
    )
    # ### end Alembic commands ###
