import React, {useState} from 'react'
import TextField from '@mui/material/TextField';
import LoginIcon from '@mui/icons-material/Login';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import '../../styles.css'

const Login = () => {
    const [username, setUsername] = useState(() => "")
    const [password, setPassword] = useState(() => "")
    const [error, setError] = useState(() => "")

    const handleUsernameChange = (e) => {
        setUsername(preUsername => e.target.value)
    }

    const handlePasswordChange = (e) => {
        setPassword(prePassword => e.target.value)
    }

    const handleSubmit = (e) => {
        e.preventDefault()
    }

    return (
        <div>
        <Typography variant="h4" className='header'>Login</Typography>
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
                <p className='error'>{error}</p>
                <div className='center-button'>
                    <Button type='submit' variant="outlined" color="success" endIcon={<LoginIcon />}>Login</Button>
                </div>
            </form>
            </Box>
            </div>
        </div>
    )
}

export default Login