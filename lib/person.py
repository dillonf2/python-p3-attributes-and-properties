#!/usr/bin/env python3

class Person:
    approved_jobs = [
        "Admin",
        "Customer Service",
        "Human Resources",
        "ITC",
        "Production",
        "Legal",
        "Finance",
        "Sales",
        "General Management",
        "Research & Development",
        "Marketing",
        "Purchasing"
    ]

    def __init__(self, name=None, age=None, job=None):
        self.name = name
        self.age = age
        self.job = job

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.capitalize()
        else:
            print("Name must be a string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_age(self):
        return self._age

    def set_age(self, age):
        if isinstance(age, int) and 0 <= age <= 120:
            self._age = age
        else:
            print("Age must be an integer between 0 and 120.")

    age = property(get_age, set_age)

    def get_job(self):
        return self._job

    def set_job(self, job):
        if job in self.approved_jobs:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)