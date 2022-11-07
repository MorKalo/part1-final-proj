import React, {useState} from 'react'
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import AddReactionOutlinedIcon from '@mui/icons-material/AddReactionOutlined';
import axios from 'axios';
import Swal from 'sweetalert2'
import '../../styles.css'

const Signup = () => {

    const [username, setUsername] = useState(() => "")
    const [password, setPassword] = useState(() => "")
    const [email, setEmail] = useState(() => "")
    const [firstName, setFirstName] = useState(() => "")
    const [lastName, setLastName] = useState(() => "")
    const [address, setAddress] = useState(() => "")
    const [phoneNumber, setPhoneNumber] = useState(() => "")
    const [creditCardNumber, setCreditCardNumber] = useState(() => "")
    const [error, setError] = useState(() => "")

    const handleUsernameChange = (e) => {
        setUsername(preUsername => e.target.value)
    }

    const handlePasswordChange = (e) => {
        setPassword(prePassword => e.target.value)
    }

    const handleEmailChange = (e) => {
        setEmail(preEmail => e.target.value)
    }

    const handleFirstNmaeChange = (e) => {
        setFirstName(preFirstName => e.target.value)
    }

    const handleLastNameChange = (e) => {
        setLastName(prePassword => e.target.value)
    }

    const handleAddressChange = (e) => {
        setAddress(preAddress => e.target.value)
    }

    const handlephoneNumberdChange = (e) => {
        setPhoneNumber(prephoneNumber => e.target.value)
    }

    const handlecreditCardNumberChange = (e) => {
        setCreditCardNumber(precreditCardNumber => e.target.value)
    }

    const handleSubmit = (e) => {
        e.preventDefault()
        const reqBody = 
        {
            user: {
                username: username,
                password: password,
                email: email,
                user_role: 1
            }, 
            customer: {
                first_name: firstName,
                last_name: lastName,
                address: address,
                phone_no: phoneNumber,
                credit_card_no: creditCardNumber,
                user_id: null
            }
            
        }
        axios.post('http://localhost:5000/signup', reqBody)
        .then(res => {
            if (res.status === 200) {
                setError(preError => '')
                Swal.fire({
                    icon: 'success',
                    title: 'New Customer has been created!',
                    showConfirmButton: false,
                    timer: 1500
                  })
                  return;
            }
        })
        .catch(err => {
            if (err.response.status === 409) {
                setError(preError => 'data is not valid')
                return;
            }
            console.log(err);
      
            Swal.fire({
            icon: 'error',
            title: 'Server error',
            text: 'Please check your connection to the server'
            })
            return;
        })

    }

    return (
        <div>
        <Typography variant="h4" className='header'>Signup</Typography>
        <div className='center'>
            <Box
            sx={{
                width: 500,
                maxWidth: '100%',
            }}
            >
            <form onSubmit={handleSubmit}>      
                <div className='center'>
                    <TextField fullWidth label='Username' variant="standard" onChange={handleUsernameChange} value={username} required/>
                </div>  
                <div className='center'>
                    <TextField fullWidth type='password' label='Password' variant="standard" onChange={handlePasswordChange} value={password} required/>
                </div>
                <div className='center'>
                    <TextField fullWidth type='email' label='Email' variant="standard" onChange={handleEmailChange} value={email} required/>
                </div>
                <div className='center'>
                    <TextField fullWidth label='First name' variant="standard" onChange={handleFirstNmaeChange} value={firstName} required/>
                </div>
                <div className='center'>
                    <TextField fullWidth label='Last name' variant="standard" onChange={handleLastNameChange} value={lastName} required/>
                </div>
                <div className='center'>
                    <TextField fullWidth label='Address' variant="standard" onChange={handleAddressChange} value={address} required/>
                </div>
                <div className='center'>
                    <TextField fullWidth label='Phone number' variant="standard" onChange={handlephoneNumberdChange} value={phoneNumber} required/>
                </div>
                <div className='center'>
                    <TextField fullWidth label='Credit Card number' variant="standard" onChange={handlecreditCardNumberChange} value={creditCardNumber} required/>
                </div>
                <p className='error'>{error}</p>
                <div className='center-button'>
                    <Button type='submit' variant="outlined" endIcon={<AddReactionOutlinedIcon />}>Signup</Button>
                </div>
            </form>
            </Box>
        </div>
        </div>
    )
}

export default Signup