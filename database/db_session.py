from contextlib import contextmanager
from sqlalchemy import inspect, func

from database.db_setup import Session


class SessionManager:
    """
    CRUD for db
    """
    @classmethod
    @contextmanager
    def session_scope(cls, obj=None, commit=True):
        """Provide a transactional scope around a series of operations."""
        session = Session()
        object_session = None
        if obj is not None:
            object_session = session.object_session(obj)
            if object_session is not None:
                session = object_session

        try:
            yield session
            if commit:
                session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def save(self):
        with self.session_scope() as session:
            self._run_callback('before_save')
            session.add(self)

    def save_with(self, *linked_instances):
        with self.session_scope() as session:
            self._run_callback('before_save')
            session.add(self)
            for instance in linked_instances:
                instance._run_callback('before_save')
                session.add(instance)

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        with self.session_scope(obj=self) as session:
            session.add(self)

    def delete(self):
        with self.session_scope(obj=self) as session:
            session.delete(self)

    def _run_callback(self, callbackname):
        callback = getattr(self, callbackname, None)
        if callback is not None:
            callback()

    @classmethod
    def delete_by(cls, filters=None, **kwargs):
        with cls.session_scope() as session:
            query = session.query(cls)
            for f in filters or []:
                query = query.filter(f)
            query.filter_by(**kwargs).delete(synchronize_session=False)

    @classmethod
    def update_by(cls, filters, new_fields):
        with cls.session_scope() as session:
            session.query(cls).filter_by(**filters).update(new_fields)

    @classmethod
    def get(cls, pk):
        with cls.session_scope(commit=False) as session:
            return session.query(cls).get(pk)

    @classmethod
    def get_all(cls, limit=None, offset=None, filters=None,
                ordering=None, columns=None, **kwargs):
        return cls._get_query(
            limit=limit,
            offset=offset,
            ordering=ordering,
            columns=columns,
            filters=filters,
            **kwargs
        ).all()

    @classmethod
    def get_sum_of_abs(cls, column, filters=None, **kwargs):
        return cls._get_query(
            columns=[func.sum(func.abs(column))],
            filters=filters,
            **kwargs
        ).scalar()

    @classmethod
    def get_first(cls, limit=None, offset=None, filters=None,
                  ordering=None, columns=None, **kwargs):
        return cls._get_query(
            limit=limit,
            offset=offset,
            ordering=ordering,
            columns=columns,
            filters=filters,
            **kwargs
        ).first()

    @classmethod
    def get_last(cls, columns=None, **kwargs):
        return cls._get_query(columns=columns, ordering=cls.created_at.desc(), **kwargs).first()


    @classmethod
    def get_count(cls, limit=None, offset=None, filters=None, **kwargs):
        return cls._get_query(filters=filters, **kwargs).count()

    @classmethod
    def get_all_from(cls, other_table, columns=None, filters=None, ordering=None, limit=None, offset=None, **kwargs):
        return cls._get_query(columns=columns, filters=filters, **kwargs).join(
            other_table).order_by(ordering).offset(offset).limit(limit).all()

    @classmethod
    def get_first_from(cls, other_table, columns=None, filters=None, ordering=None, **kwargs):
        return cls._get_query(columns=columns, filters=None, **kwargs).join(
            other_table).order_by(ordering).first()

    @classmethod
    def get_single(cls):
        return cls._get_query().first()

    @classmethod
    def get_columns(cls):
        return [c.key for c in inspect(cls).attrs]

    @classmethod
    def _get_query(cls, limit=None, offset=None, filters=None,
                   ordering=None, columns=None, **kwargs):
        kwargs = cls._prepare_kwargs(**kwargs)
        if columns is None:
            columns = [cls]
        with cls.session_scope(commit=False) as session:
            query = session.query(*columns)
            for filter_ in filters or []:
                query = query.filter(filter_)
            if ordering is None:
                return query.filter_by(**kwargs).offset(offset).limit(limit)
            return query.filter_by(**kwargs).order_by(ordering).offset(offset).limit(limit)


    @classmethod
    def _prepare_kwargs(cls, **kwargs):
        res = {}
        for k, v in kwargs.items():
            if k in cls.get_columns():
                res[k] = v
        return res
