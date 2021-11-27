import { InputGroup, FormControl, Button, Card,
  Col, Row, Container, Alert} from 'react-bootstrap';
import React, { useState } from 'react';
import {login} from './Client';
import {Context} from './Context';
import {useContext} from "react";

import { useNavigate } from "react-router-dom";

const handleChange = (f) => (event) => f(event.target.value)


export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const history = useNavigate();
  const [context, dispatch] = useContext(Context)

  const onClick = async () => {
    const data = {
      email,
      password,
    };
    try {
      const {token} = await login(data);

      console.log(data);
      dispatch({type: 'SET_TOKEN', payload: token});
      history('/profile');
    } catch(e) {
      setError(e)
    }
  }

  return (
    <Container>
      <Row style={{height: '100px'}}></Row>
      <Row>
        <Col></Col>
        <Col xs={6}>
          <Card className='md-center'>
            <Card.Header>Login</Card.Header>
            <Card.Body>
              {error !== '' ?
                <Alert variant="danger">
                {error}
                </Alert> : null
              }
              <InputGroup className="mb-3">
                <InputGroup.Text className='w-25'>Email</InputGroup.Text>
                <FormControl
                  onChange={handleChange(setEmail)}
                  aria-label="email" value={email} />
              </InputGroup>
              <InputGroup className="mb-3">
                <InputGroup.Text className='w-25'>Password</InputGroup.Text>
                <FormControl
                  onChange={handleChange(setPassword)}
                  type="password"  value={password} aria-label="password" />
              </InputGroup>

              <Button
                className='w-100' variant="primary"
                onClick={onClick}>Login</Button>


            </Card.Body>
            <Card.Footer>
              <Button
                className='w-100' variant="primary"
                onClick={() => history('/register')}>Register</Button>
            </Card.Footer>
          </Card>
        </Col>
        <Col></Col>

      </Row>
    </Container>
  )
}
