//Include modules
var express = require('express');
var handlebars = require('express-handlebars').create({defaultLayout:'main'});
var bodyParser = require('body-parser');
var mysql = require('mysql');

//Setup application
var app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(express.static('views'))
app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');
app.set('port', 6532);

//Setup database pool
var pool = mysql.createPool({
    host  : 'INSERT_HOST_ADDRESS',
    user  : 'INSERT_USER_NAME',
    password: 'INSERT_PASSWORD',
    database: 'INSERT_DATABASE_NAME'
});

//Initialize database table
app.get('/INIT_DATABASE_TABLE',function(req,res,next){
    var context = {};
    pool.query("DROP TABLE IF EXISTS workouts", function(err){
        var createString = "CREATE TABLE workouts("+
        "id INT PRIMARY KEY AUTO_INCREMENT,"+
        "name VARCHAR(255) NOT NULL,"+
        "reps INT,"+
        "weight INT,"+
        "lbs BOOLEAN,"+
        "date DATE)";
        pool.query(createString, function(err){
            context.results = "Table reset";
            res.render('workout',context);
        });
    });
});

//Handle GET workout
app.get('/',function(req,res,next){
    res.render('workout');
});

//Handle GET workout -Fill Table
app.get('/fill',function(req,res,next){
    var context = {};
    pool.query('SELECT * FROM workouts', function(err, rows, fields){
        if(err){
            next(err);
            return;
        }
        context.tableData = JSON.stringify(rows);
        res.send(context);
    });
});

//Handle POST workout -Delete row
app.post('/del',function(req,res,next){
    var context = {};
    pool.query('DELETE FROM workouts WHERE id=?', [req.body.id], function(err, rows, fields){
        if(err){
            next(err);
            return;
        }
        context.tableData = JSON.stringify(rows);
        res.send(context);
    });
});

//Handle POST workout -Add row
app.post('/',function(req,res,next){
    var context = {};

    if (req.body.name) {
        pool.query("INSERT INTO workouts (name, reps, weight, lbs, date) VALUES (?, ?, ?, ?, ?)", [req.body.name, req.body.reps, req.body.weight, req.body.lbs, req.body.date], function(err, result){
            if(err){
                next(err);
                return;
            }
            pool.query('SELECT * FROM workouts WHERE id=?', [result.insertId], function(err, rows, fields){
                if(err){
                    next(err);
                    return;
                }
                context.tableData = JSON.stringify(rows);
                res.send(context);
            });
        });
    } else {
        context.errMsg = "You must enter a name for the workout.";
        res.send(context);
    }
});

//Handle POST update
app.post('/update',function(req,res,next){
    var context = {};
    pool.query("SELECT * FROM workouts WHERE id=?", [req.body.id], function(err, result){
        if (err) {
            next(err);
            return;
        }
        if (result.length == 1){
            var curData = result[0];
            pool.query("UPDATE workouts SET name=?, reps=?, weight=?, lbs=?, date=? WHERE id=?",
                [req.body.name || curData.name, req.body.reps || curData.reps, req.body.weight || curData.weight, req.body.lbs || curData.lbs, req.body.date || curData.date, req.body.id],
                function(err, result){
                    if (err) {
                        next(err);
                        return;
                    }
                }
            );
        }
    });
    pool.query('SELECT * FROM workouts WHERE id=?', [req.body.id], function(err, rows, fields){
        if(err){
            next(err);
            return;
        }
        context.tableData = JSON.stringify(rows);
        res.send(context);
    });
});

//Page Not Found Router
app.use(function(req,res){
    res.status(404);
    res.render('error404');
});

//Server Error Router
app.use(function(err, req, res, next){
    console.error(err.stack);
    res.type('plain/text');
    res.status(500);
    res.render('error500');
});

app.listen(app.get('port'), function(){
    console.log('Express started on http://localhost:' + app.get('port') + '; press Ctrl-C to terminate.');
});