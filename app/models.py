# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = no-member
# pylint: disable = redefined-builtin
# pylint: disable = too-few-public-methods
# pylint: disable = too-many-arguments
# pylint: disable = too-many-instance-attributes

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import ForeignKey

db = SQLAlchemy()

# many-to-many relationship tables
character_series = db.Table('character_series',
                            db.Column(
                                'character_id', db.Integer, ForeignKey('character.id')),
                            db.Column(
                                'series_id', db.Integer, ForeignKey('series.id'))
                           )
comic_series = db.Table('comic_series',
                        db.Column(
                            'comic_id', db.Integer, ForeignKey('comic.id')),
                        db.Column(
                            'series_id', db.Integer, ForeignKey('series.id'))
                       )
creator_series = db.Table('creator_series',
                          db.Column(
                              'creator_id', db.Integer, ForeignKey('creator.id')),
                          db.Column(
                              'series_id', db.Integer, ForeignKey('series.id'))
                         )
event_series = db.Table('event_series',
                        db.Column(
                            'event_id', db.Integer, ForeignKey('event.id')),
                        db.Column(
                            'series_id', db.Integer, ForeignKey('series.id'))
                       )
character_event = db.Table('character_event',
                           db.Column(
                               'character_id', db.Integer, ForeignKey('character.id')),
                           db.Column(
                               'event_id', db.Integer, ForeignKey('event.id'))
                          )
comic_event = db.Table('comic_event',
                       db.Column(
                           'comic_id', db.Integer, ForeignKey('comic.id')),
                       db.Column(
                           'event_id', db.Integer, ForeignKey('event.id'))
                      )

creator_event = db.Table('creator_event',
                         db.Column(
                             'creator_id', db.Integer, ForeignKey('creator.id')),
                         db.Column(
                             'event_id', db.Integer, ForeignKey('event.id'))
                        )
character_comic = db.Table('character_comic',
                           db.Column(
                               'character_id', db.Integer, ForeignKey('character.id')),
                           db.Column(
                               'comic_id', db.Integer, ForeignKey('comic.id'))
                          )
comic_creator = db.Table('comic_creator',
                         db.Column(
                             'comic_id', db.Integer, ForeignKey('comic.id')),
                         db.Column(
                             'creator_id', db.Integer, ForeignKey('creator.id'))
                        )



# Models a series object.
class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    desc = db.Column(db.String(1300))
    start = db.Column(db.Integer)
    end = db.Column(db.Integer)
    img = db.Column(db.String(150))
    num_creators = db.Column(db.Integer)
    num_characters = db.Column(db.Integer)
    num_comics = db.Column(db.Integer)
    num_events = db.Column(db.Integer)

    characters = db.relationship(
        'Character', secondary=character_series, backref=db.backref('series', lazy='dynamic'))
    comics = db.relationship(
        'Comic', secondary=comic_series, backref=db.backref('series', lazy='dynamic'))
    creators = db.relationship(
        'Creator', secondary=creator_series, backref=db.backref('series', lazy='dynamic'))
    events = db.relationship(
        'Event', secondary=event_series, backref=db.backref('series', lazy='dynamic'))



# Models a Character object
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    desc = db.Column(db.String(1300))
    img = db.Column(db.String(150))
    num_comics = db.Column(db.Integer)
    num_series = db.Column(db.Integer)
    num_events = db.Column(db.Integer)

    events = db.relationship(
        'Event', secondary=character_event, backref=db.backref('characters', lazy='dynamic'))
    comics = db.relationship(
        'Comic', secondary=character_comic, backref=db.backref('characters', lazy='dynamic'))

# Models an Event object
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    desc = db.Column(db.String(1300))
    img = db.Column(db.String(150))
    num_creators = db.Column(db.Integer)
    num_characters = db.Column(db.Integer)
    num_comics = db.Column(db.Integer)
    num_series = db.Column(db.Integer)

    creators = db.relationship(
        'Creator', secondary=creator_event, backref=db.backref('events', lazy='dynamic'))
    comics = db.relationship(
        'Comic', secondary=comic_event, backref=db.backref('events', lazy='dynamic'))


# Models a Creator object
class Creator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150))
    img = db.Column(db.String(150))
    num_comics = db.Column(db.Integer)
    num_series = db.Column(db.Integer)
    num_events = db.Column(db.Integer)

    comics = db.relationship(
        'Comic', secondary=comic_creator, backref=db.backref('creators', lazy='dynamic'))



# Models a Comic object
class Comic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    issue_num = db.Column(db.Integer)
    desc = db.Column(db.String(2500))
    upc = db.Column(db.String(30))
    pg_ct = db.Column(db.Integer)
    price = db.Column(db.Float)
    img = db.Column(db.String(150))
    num_creators = db.Column(db.Integer)
    num_characters = db.Column(db.Integer)
    num_events = db.Column(db.Integer)
