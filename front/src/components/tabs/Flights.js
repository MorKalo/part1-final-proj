import React, { useState } from 'react';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TablePagination from '@mui/material/TablePagination';
import TableRow from '@mui/material/TableRow';
import InputSelect from '../input-elements/inputSelect';
import Button from '@mui/material/Button';
import FlightLandOutlinedIcon from '@mui/icons-material/FlightLandOutlined';
import FlightTakeoffOutlinedIcon from '@mui/icons-material/FlightTakeoffOutlined';
import '../../styles.css'

const columns = [
  { id: 'airline', label: 'Airline', minWidth: 170 },
  { id: 'origin_country', label: 'Origin Country', minWidth: 100 },
  { id: 'destination_country', label: 'Destination Country', minWidth: 100 },
  { id: 'departure_time', label: 'Departure Time', minWidth: 100 },
  { id: 'landing_time', label: 'Landing Time', minWidth: 100 },
  { id: 'remaining_tickets', label: 'Remaining Tickets', minWidth: 100 }
];

const createData = (airline, origin_country, destination_country, departure_time, landing_time, remaining_tickets) => {
  return { airline, origin_country, destination_country, departure_time, landing_time, remaining_tickets};
}

const Flights = () => {

  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(10);
  const [rows, setRows] = useState(() => [])

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const navigateToDeparturesArrivals = () => {
    window.location.replace('http://localhost:5000/flights/tables')
    
  }

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(+event.target.value);
    setPage(0);
  };

  return (
    <div>
    <Button style={{marginLeft: "50px", marginTop: "30px"}} variant="outlined" onClick={navigateToDeparturesArrivals} startIcon={<FlightTakeoffOutlinedIcon />} endIcon={<FlightLandOutlinedIcon />} color="secondary">Departures & Arrivals</Button>
    <div className='table-center'>
    <InputSelect label="Filter by Airline" handleChange={setRows} createData={createData}/>
    </div>
    <div className='table-center'>
    <Paper sx={{ width: '100%', overflow: 'hidden' }}>
      <TableContainer sx={{ maxHeight: 440 }}>
        <Table stickyHeader aria-label="sticky table">
          <TableHead>
            <TableRow>
              {columns.map((column) => (
                <TableCell
                  key={column.id}
                  align={column.align}
                  style={{ minWidth: column.minWidth }}
                >
                  {column.label}
                </TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
            {rows
              .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
              .map((row) => {
                return (
                  <TableRow hover role="checkbox" tabIndex={-1} key={row.code}>
                    {columns.map((column) => {
                      const value = row[column.id];
                      return (
                        <TableCell key={column.id} align={column.align}>
                          {column.format && typeof value === 'number'
                            ? column.format(value)
                            : value}
                        </TableCell>
                      );
                    })}
                  </TableRow>
                );
              })}
          </TableBody>
        </Table>
      </TableContainer>
      <TablePagination
        rowsPerPageOptions={[10, 25, 100]}
        component="div"
        count={rows.length}
        rowsPerPage={rowsPerPage}
        page={page}
        onPageChange={handleChangePage}
        onRowsPerPageChange={handleChangeRowsPerPage}
      />
    </Paper>
    </div>
    </div>
  );
}

export default Flights