# -*- coding: utf-8 -*-

from flask import render_template, request, url_for, redirect
from app import app, db
from app.models import CarRole
from app.forms import Car, FindCar

page = 1


@app.route('/', methods=['GET', 'POST'])
def index():
    find_car_form = FindCar()
    if find_car_form.submit.data and find_car_form.type.data or find_car_form.manufacturer.data\
            or find_car_form.grade.data or find_car_form.seat.data or find_car_form.displacement.data \
            or find_car_form.gearbox.data or find_car_form.colour.data or find_car_form.price.data:
        cars = CarRole.query
        if find_car_form.type.data:
            cars = cars.filter(CarRole.type == find_car_form.type.data)
        if find_car_form.manufacturer.data:
            cars = cars.filter(CarRole.manufacturer == find_car_form.manufacturer.data)
        if find_car_form.grade.data:
            cars = cars.filter(CarRole.grade == find_car_form.grade.data)
        if find_car_form.seat.data:
            cars = cars.filter(CarRole.seat == find_car_form.seat.data)
        if find_car_form.displacement.data:
            cars = cars.filter(CarRole.displacement == find_car_form.displacement.data)
        if find_car_form.gearbox.data:
            cars = cars.filter(CarRole.gearbox == find_car_form.gearbox.data)
        if find_car_form.colour.data:
            cars = cars.filter(CarRole.colour == find_car_form.colour.data)
        if find_car_form.price.data:
            cars = cars.filter(CarRole.price == find_car_form.price.data)
        cars_part = cars.all()
    else:
        cars_part = CarRole.query.paginate(page, 15, False).items
    for _ in range(15 - len(cars_part)):  # 如果当前页不足15行则补全15行
        cars_part += [0]
    return render_template("home.html", cars_part=cars_part, form=find_car_form, page=page)


@app.route('/delete_car/<car_id>', methods=['GET', 'POST'])
def delete_car(car_id):
    car = CarRole.query.get(car_id)
    db.session.delete(car)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    add_car_form = Car()
    if add_car_form.submit.data:
        car_type = add_car_form.type.data
        car_manufacturer = add_car_form.manufacturer.data
        car_grade = add_car_form.grade.data
        car_seat = add_car_form.seat.data
        car_displacement = add_car_form.displacement.data
        car_gearbox = add_car_form.gearbox.data
        car_colour = add_car_form.colour.data
        car_price = add_car_form.price.data
        new_car = CarRole(type=car_type, manufacturer=car_manufacturer, grade=car_grade, seat=car_seat,
                          displacement=car_displacement, gearbox=car_gearbox, colour=car_colour, price=car_price)
        db.session.add(new_car)
        db.session.commit()
    return render_template("add.html", form=add_car_form)


@app.route('/set/<car_id>', methods=['GET', 'POST'])
def set(car_id):
    set_car_form = Car()
    car = CarRole.query.get(car_id)
    if set_car_form.submit.data:
        car.type = set_car_form.type.data
        car.manufacturer = set_car_form.manufacturer.data
        car.grade = set_car_form.grade.data
        car.seat = set_car_form.seat.data
        car.displacement = set_car_form.displacement.data
        car.gearbox = set_car_form.gearbox.data
        car.colour = set_car_form.colour.data
        car.price = set_car_form.price.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("set.html", form=set_car_form, car=car)


@app.route('/next', methods=['GET', 'POST'])
def next_page():
    global page
    if page < CarRole.query.paginate(page, 15, False).pages:
        page += 1
    return redirect(url_for('index'))


@app.route('/Previous', methods=['GET', 'POST'])
def previous_page():
    global page
    if page > 1:
        page -= 1
    return redirect(url_for('index'))
