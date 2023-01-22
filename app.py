<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Калькулятор</title>
</head>
<body onLoad="initialize()">

    <div class="wrapper">

        <form name="calc" action="">
        <div class="container">
            <div class="form-wrapper">
                <div class="form-wrapper__item">
                    <input type="text" id="val1" class="input" placeholder="First value">
                </div>
                <div class="form-wrapper__item">
                    <select name="operator" class="custom-select"  id="inputGroupSelect01">
                        <option value="plus">+</option>
                        <option value="minus">-</option>
                        <option value="divide">/</option>
                        <option value="multiply">*</option>
                        <option selected>Choose operator</option>
                    </select>
                </div>
                <div class="form-wrapper__item">
                    <input type="text" id="val2" name="val2" class="input" placeholder="Second value">
                </div>
                <div class="form-wrapper__item">
                    <button type="button" class="btn" value="answer" onClick="calculate('val1','val2')">CALCULATE</button>
                </div>
                <div class="form-wrapper__item">
                    <input type="text"  name="answer" class="input" placeholder="Result">
                </div>
            </div>
        </div>
    </form>
    </div>
    <script src="script.js"></script>
</body>
</html>