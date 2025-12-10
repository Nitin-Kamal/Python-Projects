conv1 = ''
while conv1.upper() != "QUIT":
    conv1 = input('what type of conversion do u need?:(A)rea or (P)erimeter or (C)ircumference or (F)ormula or quit to quit: ')
    if conv1.upper() == "QUIT":
        print('ok, see you again!')
        break
    aconv = ''
    if conv1.upper() == "A":
        aconv = input('which shape do u want to find the area for:(S)quare or (R)ectangle? or (C)ircle: ')
    if aconv.upper() == "S":
        aconvs = int(input('what is the measurement of the sides of your square?: '))
        aconvtype = input('what measurement type is this, M for meter and CM for centimeter: ')
        squareans = aconvs * aconvs
        print(f"the answer is: {squareans} {aconvtype.upper()}^2")
    elif aconv.upper() == "R":
        aconvr = int(input('what is the length of your rectangle: '))
        aconvr1 = int(input('what is the breadth of your rectangle: '))
        aconvtyper = input('what measurement type is this, M for meter and CM for centimeter: ')
        rectans = aconvr * aconvr1
        print(f"the answer is: {rectans} {aconvtyper.upper()}^2")
    elif aconv.upper() == "C":
        aconvc = int(input("What is the radius of your circle: "))
        aconvctype = input("What type of measurement unit is the radius in: ")
        circans = 3.142857142857 * (aconvc ** 2)
        print(f"The area of your circle is: {circans} {aconvctype.upper()}^2")
    pconv = ""
    if conv1.upper() == "P":
        pconv = input('what shape do u want to find the perimeter for:(S)quare or (R)ectangle: ')
    if pconv.upper() == "S":
        pconvs = int(input('what is the measurement of the sides of your square: '))
        pconvtype = input('what measurement type is this, M for meter and CM for centimeter: ')
        squareans1 = pconvs * 4
        print(f"the answer is: {squareans1} {pconvtype.upper()}")
    elif pconv.upper() == "R":
        pconvr = int(input('what is the length of your rectangle: '))
        pconvr1 = int(input('what is the breadth of your rectangle: '))
        pconvtyper = input('what measurement type is this, M for meter and CM for centimeter: ')
        rectans1 = pconvr + pconvr1
        rectans2 = rectans1 * 2
        print(f"the answer is: {rectans2} {pconvtyper.upper()}")
    cconv = ""
    if conv1.upper() == "C":
        cconv = int(input('what is the radius of your circle: '))
        cconv_result = 2 * 3.14 * cconv
        cconvtype = input('what measurement type is this, M for meter and CM for centimeter: ')
        print(f"your circle's circumference is {cconv_result}{cconvtype}")

    fconv = ''
    if conv1.upper() == "F":
        fconv = input('what shape do u want the formula for square, rectangle or circle: ')
    fconvas = ''
    fconvar = ''
    fconvac = ''
    if fconv.upper() == "SQUARE":
        fconvas = input('do u want the formula for area of a square or perimeter of a square: ')
    if fconvas.upper() ==  "AREA OF A SQUARE":
        print('the formula for area of a square is side X side')
    elif fconvas.upper() == "PERIMETER OF A SQUARE":
        print('the formula for perimeter of a square is 4 X a or 4 X side')
    if fconv.upper() == "RECTANGLE":
        fconvar = input('do u want the formula for area of a rectangle or perimeter of a rectangle: ')
    if fconvar.upper() == "AREA OF A RECTANGLE":
        print('the formula for area of a rectangle is length X breadth')
    elif fconvar.upper() == "PERIMETER OF A RECTANGLE":
        print('the formula for perimeter of a rectangle is 2 X length + breadth')
    if fconv.upper() == "CIRCLE":
        fconvac = input('do u want the formula for area of a circle or circumference of a circle: ')
    if fconvac.upper() == "AREA OF A CIRCLE" or fconvac.upper() == "AREA":
        print('the formula for area of a circle is π r²')
    elif fconvac.upper() == "CIRCUMFERENCE OF A CIRCLE" or fconvac.upper() == "CIRCUMFERENCE":
        print('the formula for circumference of a circle is 2πr')