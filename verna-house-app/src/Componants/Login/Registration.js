
import React from 'react';

import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import { useNavigate, Link } from "react-router-dom";
import IconButton from '@mui/material/IconButton';
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import classes from '../Login.module.css';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Select from '@mui/material/Select';
import OutlinedInput from '@mui/material/OutlinedInput';
import InputLabel from '@mui/material/InputLabel';
import InputAdornment from '@mui/material/InputAdornment';
import FormHelperText from '@mui/material/FormHelperText';
import FormControl from '@mui/material/FormControl';
import Visibility from '@mui/icons-material/Visibility';
import VisibilityOff from '@mui/icons-material/VisibilityOff';
import MenuItem from '@mui/material/MenuItem';
import { makeStyles, ThemeProvider } from "@material-ui/core/styles";
import { formatMuiErrorMessage } from '@mui/utils';
import { useForm, Controller } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as Yup from 'yup';






const useStyles = makeStyles({
    root1: {
        color: '#121212',
        '&:hover': {
            color: '#EC255A',
        }
    },
    root2: {
        '&:onClick': {
            color: '#121212',
        },
        color: '#EC255A',
        '&:hover': {
            color: '#121212',
        },
        '&:active': {
            color: '#EC255A',
        }
    },
    root3: {
        color: '#EC255A',
        '&:hover': {
            color: '#121212',
        }
    },
    root4:
    {
        background: 'linear-gradient(45deg, #FFE3E3 25%, #F3C5C5 80%)',
        color: 'action.home',
    },
});

const Rolls = [
    {
        value: 'Supplier',
        label: 'Supplier',
    },
    {
        value: 'Customer',
        label: 'Customer',
    },
    {
        value: 'Agency',
        label: 'Agency',
    },
    {
        value: 'Worker',
        label: 'Worker',
    },
];

const Registration = props => {
    const navigate = useNavigate()
    
    const validationSchema = Yup.object().shape({
        fullname: Yup.string().required('Fullname is required'),
        username: Yup.string()
            .required('Username is required')
            .min(6, 'Username must be at least 6 characters')
            .max(20, 'Username must not exceed 20 characters')
        email: Yup.string()
            .required('Email is required')
            .email('Email is invalid'),
        password: Yup.string()
            .required('Password is required')
            .min(6, 'Password must be at least 6 characters')
            .max(40, 'Password must not exceed 40 characters'),
        confirmPassword: Yup.string()
            .required('Confirm Password is required')
            .oneOf([Yup.ref('password'), null], 'Confirm Password does not match'),
        acceptTerms: Yup.bool().oneOf([true], 'Accept Terms is required')
    });
    const { register, control, handleSubmit, formState: { errors } } = useForm({
        resolver: yupResolver(validationSchema)
    });

    const onSubmit = data => {
        console.log(JSON.stringify(data, null, 2));
    };
    const goBackHandler = () => {
        navigate("/Login")
    }

    const classes1 = useStyles();
    const [values, setValues] = React.useState({
        name: '',
        email: '',
        username: '',
        password: '',
        confirm: '',
        // weight: '',
        // weightRange: '',
        showPassword: false,
    });

    const handleChange = (prop) => (event) => {
        setValues({ ...values, [prop]: event.target.value });
    };

    const handleClickShowPassword = () => {
        setValues({
            ...values,
            showPassword: !values.showPassword,
        });
    };

    const onRegisterHandler = (e) => {
        e.preventDefault()
        // dispatch({LoggedInReducer})
    }

    const handleMouseDownPassword = (event) => {
        event.preventDefault();
    };

    const [roll, setRoll] = React.useState(null);

    const rollChangeHandler = (event) => {
        setRoll(event.target.value);
    };


    return (
        <Container align="center">
            <Card variant="outlined"
                sx={{
                    maxWidth: 500, maxHeight: 8000, background: 'linear-gradient(45deg, #F3C5C5 30%, #FFE3E3 50%,#F3C5C5 30%,#FFE3E3 50%)',
                    borderColor: '#EC255A',
                    borderWidth: 1,
                    borderRadius: 5,
                    color: 'action.home',
                    paddingTop: 1,
                    m: 1,
                    marginTop: 3
                }}
                >
                <CardActions>
                    <IconButton sx={{ marginLeft: 1, }} onClick={goBackHandler} className={classes1.root1}>
                        <ChevronLeftIcon className={classes1.root1}/>
                    </IconButton>
                </CardActions>
                <CardContent>
                    <Typography variant="h4" component='div' fontSize='26px' className={classes.registration}>Register Here</Typography>
                    <Box
                        component="form"
                        sx={{
                            marginTop: 5,
                            marginLeft: 0,
                            '& .MuiTextField-root': { m: 1, width: '40ch' },
                        }}
                        noValidate
                        autoComplete="off"
                        onSubmit={onRegisterHandler}
                    >
                        <div>
                            <TextField
                                required
                                multiline
                                size='medium'
                                id="fullname"
                                label="Enter Your Name"
                                placeholder="xyz abc"
                                {...register('fullname')}
                                error={errors.fullname ? true: false}
                            />
                            <Typography variant="inherit" color="textSecondary">
                                {errors.fullname?.message}
                            </Typography>
                            <TextField
                                required
                                multiline
                                size='medium'
                                id="email"
                                label="Enter Your Email Address"
                                placeholder="xyz@abc.com"
                                {...register('email')}
                                error={errors.email ? true : false}
                            />
                            <Typography variant="inherit" color="textSecondary">
                                {errors.email?.message}
                            </Typography>
                            <TextField
                                required
                                multiline
                                size='medium'
                                id="username"
                                label="Enter Your UserName"
                                placeholder="xyz_abc123"
                                {...register('username')}
                                error ={errors.username?true:false}
                            />
                            <Typography variant="inherit" color="textSecondary">
                                {errors.username?.message}
                            </Typography>
                            <FormControl required sx={{ m: 1, width: '40ch' }} variant="outlined" autoComplete="current-password">
                                <InputLabel htmlFor="outlined-adornment-password">Enter New Password</InputLabel>
                                <OutlinedInput
                                    label="Enter New Password"
                                    placeholder='*******'
                                    id="newpassword"
                                    type={values.showPassword ? 'text' : 'password'}
                                    value={values.password}
                                    onChange={handleChange('password')}
                                    endAdornment={
                                        <InputAdornment position="end">
                                            <IconButton
                                                className={classes1.root1}
                                                aria-label="toggle password visibility"
                                                onClick={handleClickShowPassword}
                                                onMouseDown={handleMouseDownPassword}
                                                edge="end"
                                            >
                                                {values.showPassword ? <VisibilityOff className={classes1.root1} /> : <Visibility className={classes1.root1}/>}
                                            </IconButton>
                                        </InputAdornment>
                                    }
                                    {...register('newpassword')}
                                    error={errors.newpassword ? true : false}
                                />
                                <Typography variant="inherit" color="textSecondary">
                                    {errors.newpassword?.message}
                                </Typography>
                            </FormControl>
                            <TextField
                                required
                                label="Enter Confirm Password"
                                placeholder='*******'
                                id="confirmpassword"
                                type={values.showPassword ? 'text' : 'password'}
                                value={values.password}
                                onChange={handleChange('password')}
                                InputProps={{
                                    endAdornment: (
                                        <InputAdornment position="end">
                                            <IconButton
                                                className={classes1.root1}
                                                aria-label="toggle password visibility"
                                                onClick={handleClickShowPassword}
                                                onMouseDown={handleMouseDownPassword}
                                                edge="end"
                                            >
                                                {values.showPassword ? <VisibilityOff className={classes1.root1} /> : <Visibility className={classes1.root1}/>}
                                            </IconButton>
                                        </InputAdornment>
                                    )
                                }}
                                {...register('confirmPassword')}
                                error={errors.confirmPassword ? true : false}
                            />
                            <Typography variant="inherit" color="textSecondary">
                                {errors.confirmPassword?.message}
                            </Typography>
                            <FormControl required sx={{ m: 1, width: '40ch' }} >
                                <InputLabel id="roll-id">Roll</InputLabel>
                                <Select
                                    sx={{ textAlign: 'left'}}
                                    labelId="demo-simple-select-label"
                                    id="select-roll"
                                    label="Roll"
                                    value={roll}
                                    onChange={rollChangeHandler}
                                >
                                    {Rolls.map((option) => (
                                        <MenuItem key={option.value} value={option.value}>
                                            {option.label}
                                        </MenuItem>
                                    ))}
                                </Select>
                                <FormHelperText>Please select your roll in system.</FormHelperText>
                            </FormControl>

                            <div className={classes.button}>
                                <Button
                                    className={classes1.root4}
                                    variant="contained"
                                    onClick={handleSubmit(onSubmit)}
                                    sx={{
                                        marginTop: 0.5,
                                        marginRight: -34,
                                        color: 'black',
                                    }}>
                                    Sign Up</Button>
                            </div>
                            <div className={classes.register}>
                                <Typography variant="body1" sx={{ marginTop: 0.5, marginLeft: -13.5, color:'black' }}>
                                    Do You Have An Account?
                                    <Link to={"/Login"} className={classes1.root3}> Sign In  </Link>
                                </Typography>
                                <Typography variant="body1" sx={{ marginTop: 0.5, marginLeft: -27, color: 'black'    }}>
                                    <Link to={"/Registration"} className={classes1.root3}>Forgot Password?
                                    </Link>
                                </Typography>
                            </div>
                        </div>
                    </Box>
                </CardContent>
            </Card>
        </Container>
    );

};
export default Registration;

/*

<FormControl required sx={{ m: 1, width: '40ch' }} variant="outlined" >
                                <InputLabel htmlFor="outlined-adornment-password">Enter Confirm Password</InputLabel>
                                <OutlinedInput
                                    label="Enter Confirm Password"
                                    placeholder='*******'
                                    id="confirm-password"
                                    type={values.showPassword ? 'text' : 'password'}
                                    value={values.password}
                                    onChange={handleChange('password')}
                                    endAdornment={
                                        <InputAdornment position="end">
                                            <IconButton
                                                aria-label="toggle password visibility"
                                                onClick={handleClickShowPassword}
                                                onMouseDown={handleMouseDownPassword}
                                                edge="end"
                                            >
                                                {values.showPassword ? <VisibilityOff /> : <Visibility />}
                                            </IconButton>
                                        </InputAdornment>
                                    }
                                />
                            </FormControl>
*/