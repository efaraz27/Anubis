import React from 'react';

import NavItem from './NavItem';

const Nav = () => {
  return (
    <div className='flex flex-row justify-between align-center space-x-8'>
      <NavItem path={'/getstarted'}>Get Started</NavItem>
      <NavItem path={'/platform'}> Platform </NavItem>
      <NavItem path={'/blog'}>Blog</NavItem>
      <div className='border-l-2 border-gray opacity-60'>{" "}</div>
      <NavItem path={'/redirect?to=signin'}>Sign In</NavItem>
    </div>
  )
}

export default Nav;
