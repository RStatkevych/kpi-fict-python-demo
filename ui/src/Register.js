import { InputGroup, FormControl, Button, Card,
  Col, Row, Container } from 'react-bootstrap';
import React, { useState } from 'react';
import {register} from './Client'

import { useNavigate } from "react-router-dom";

const handleChange = (f) => (event) => f(event.target.value)


export default function Register() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [name, setName] = useState('');
  const history = useNavigate();

  const onClick = async () => {
    const data = {
      email,
      password,
      name,
      confirm: confirmPassword
    };
    console.log(data);
    await register(data);
    history('/login');
  }

  return (
    <Container>
      <Row style={{height: '100px'}}></Row>
      <Row>
        <Col></Col>
        <Col xs={6}>
          <Card className='md-center'>
            <Card.Header>Register</Card.Header>
            <Card.Body>
              <InputGroup className="mb-3">
                <InputGroup.Text className='w-25'>Email</InputGroup.Text>
                <FormControl
                  onChange={handleChange(setEmail)}
                  aria-label="email" value={email} />
              </InputGroup>
              <InputGroup className="mb-3">
                <InputGroup.Text className='w-25'>Name</InputGroup.Text>
                <FormControl
                  onChange={handleChange(setName)}
                  aria-label="name"  value={name}/>
              </InputGroup>
              <InputGroup className="mb-3">
                <InputGroup.Text className='w-25'>Password</InputGroup.Text>
                <FormControl
                  onChange={handleChange(setPassword)}
                  type="password"  value={password} aria-label="password" />
              </InputGroup>
              <InputGroup className="mb-3">
                <InputGroup.Text className='w-25'>Confirm Password</InputGroup.Text>
                <FormControl
                  onChange={handleChange(setConfirmPassword)}
                  type="password"
                  value={confirmPassword} aria-label="confirm_password" />
              </InputGroup>
              <Button
                className='w-100' variant="primary"
                onClick={onClick}>Register</Button>

            </Card.Body>
            <Card.Footer>
              <Button
                className='w-100' variant="primary"
                onClick={() => history('/login')}>Login</Button>
            </Card.Footer>

          </Card>
        </Col>
        <Col></Col>

      </Row>
    </Container>
  )
}
