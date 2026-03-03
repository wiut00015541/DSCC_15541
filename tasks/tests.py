import pytest
from django.contrib.auth.models import User
from tasks.models import Task, Category, Tag


@pytest.mark.django_db
def test_create_category():
    category = Category.objects.create(name="Work")
    assert category.name == "Work"


@pytest.mark.django_db
def test_create_tag():
    tag = Tag.objects.create(name="Urgent")
    assert tag.name == "Urgent"


@pytest.mark.django_db
def test_create_task():
    user = User.objects.create_user(username="testuser", password="12345")
    category = Category.objects.create(name="Home")

    task = Task.objects.create(
        title="Test Task",
        description="Test Description",
        category=category,
        owner=user,  # <-- исправлено
    )

    assert task.title == "Test Task"


@pytest.mark.django_db
def test_task_category_relationship():
    user = User.objects.create_user(username="user2", password="12345")
    category = Category.objects.create(name="Study")

    task = Task.objects.create(
        title="Read", description="Book", category=category, owner=user  # <-- добавлено
    )

    assert task.category.name == "Study"


@pytest.mark.django_db
def test_task_tag_relationship():
    user = User.objects.create_user(username="user3", password="12345")
    tag = Tag.objects.create(name="Important")

    task = Task.objects.create(
        title="Task", description="Desc", owner=user  # <-- добавлено
    )

    task.tags.add(tag)

    assert task.tags.count() == 1
