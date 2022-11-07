import React from 'react';
import { Link } from 'react-router-dom';
import '../styles.css'


export const Navbar = () => {
    return (
        <div>
            <nav className='nav'>
                <a className="site-title">Fine Flighs</a>
                <ul>
                    <Link to="/flights">Flights</Link>
                    <Link to="/airlines">Airline Companies</Link>
                    <Link to="/login">Login</Link>
                    <Link to="/signup">Signup</Link>
                </ul>
            </nav>
        </div>
    )
}