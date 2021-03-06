#!/usr/bin/env python
# coding=utf-8

import os

basedir = os.path.abspath(os.path.dirname(__file__))
datadir = os.path.join(basedir, "data")


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SUPERVISOR_MAIL_SENDER = 'admin@example.com'
    SUPERVISOR_ADMIN = os.environ.get('SUPERVISOR_ADMIN') or "admin"

    SCHEDULER_API_ENABLED = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('ADMIN_WEB_DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(datadir, 'data-dev.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('ADMIN_WEB_TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(datadir, 'data-test.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('ADMIN_WEB_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(datadir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'prodection': ProductionConfig,

    'default': DevelopmentConfig
}
