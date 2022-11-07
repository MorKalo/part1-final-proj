import React, { useState, useEffect } from 'react'
import axios from "axios";
import '../../styles.css'
import Airline from '../resourses/Airline';
import Typography from '@mui/material/Typography';


export const Airlines = () => {

  const [airlines, SetAirlines] = useState(() => [])

  useEffect(() => {
    axios.get('http://localhost:5000/airlines').then((response) => {
      console.log(response);
      if (response.status  ===  200) SetAirlines(lastAirlines => response.data.data);
      console.log(response.data.data);
    }).catch(err => {
      console.log(err);
    })
  }, [])

  return (
    <div>
        <Typography variant="h3" className='header'>Our Airlines</Typography>
        <div className='center'>
        {airlines.map(airline => <Airline key={airline.id} country={airline.country} name={airline.name}/>
       )}
       </div>
    </div>
  )
}