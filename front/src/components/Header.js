import React from 'react'
import { Route, Routes } from 'react-router-dom';
import { Airlines } from './tabs/Airlines';
import Login from './tabs/Login';
import Signup from './tabs/Signup';
import Flights from './tabs/Flights';
import { Navbar } from './Navbar';



export const Header = () => {
  return (
    <div>
      <Navbar />
        <Routes>
            <Route path='/' element={<Flights />} />
            <Route path='/airlines' element={<Airlines />} />
            <Route path='/flights' element={<Flights />} />
            <Route path='/login' element={<Login />} />
            <Route path='/signup' element={<Signup />} />
        </Routes>
    </div>
  )
}