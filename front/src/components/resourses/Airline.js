import React, { useEffect, useState } from 'react';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import axios from 'axios';


const InputSelect = (props) => {

    const [airline, setAirline] = useState(() => '')
    const [allAirlines, setAllAirlines] = useState(() => [])

    useEffect(() => {
        axios.get('http://localhost:5000/airlines').then(res => {
                setAllAirlines(lastAirlines => res.data.data)
            })
            .catch(err => {
                console.log(err);
            }) 
        }, [])

    const handleSelect = (e) => {
        console.log(e.target)
        setAirline(e.target.value);
        if (e.target.value === 'All Airlines') {
            axios.get('http://localhost:5000/flights').then(res => {
                const flights = res.data.data
                const newRows = []
                flights.forEach(flight => newRows.push(props.createData(flight.airline_company, flight.origin_country, flight.destination_country, 
                    flight.departure_time, flight.landing_time, flight.remaining_tickets)))
                    props.handleChange(lastRows => newRows)
            })
            .catch(err => {
                console.log(err);
            })
        }
        else {
            axios.get(`http://localhost:5000/flights?airline_id=${e.target.value}`).then(res => {
                const flights = res.data.data
                const newRows = []
                flights.forEach(flight => newRows.push(props.createData(flight.airline_company, flight.origin_country, flight.destination_country, 
                    flight.departure_time, flight.landing_time, flight.remaining_tickets)))
                    props.handleChange(lastRows => newRows)
            })
            .catch(err => {
                console.log(err);
            })
        }
    }

    return (
        <div>
            <FormControl variant="standard" fullWidth>
            <InputLabel id="demo-simple-select-label">{props.label}</InputLabel>
            <Select
                labelId="demo-simple-select-label"
                id="demo-simple-select"
                value={airline}
                label={props.label}
                onChange={handleSelect}
            >
                <MenuItem value="All Airlines" key={0}>All Airlines</MenuItem>
                {allAirlines.map(airline => <MenuItem value={airline.id} key={airline.id}>{airline.name}</MenuItem>)}
            </Select>
            </FormControl>
        </div>
    );
    }

export default InputSelect;