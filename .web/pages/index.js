
/** @jsxImportSource @emotion/react */import { Fragment } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Box, Center, Flex, Heading, HStack, Image as ChakraImage, Link, Spacer, Text, VStack } from "@chakra-ui/react"
import "focus-visible/dist/focus-visible"
import NextLink from "next/link"
import NextHead from "next/head"



export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <Box>
  <VStack sx={{"bg": "#212529", "position": "sticky", "borderBottom": "0.25em solid #D3D3D3", "paddingX": "2em", "paddingY": "1em", "zIndex": "999", "top": "0", "width": "100%"}}>
  <HStack sx={{"width": "100%"}}>
  <ChakraImage alt={`Logo juanma`} src={`logojuan.png`} sx={{"width": "4em", "height": "4em"}}/>
  <Text>
  {`Juanma´s Page`}
</Text>
  <Spacer/>
  <Link as={NextLink} className={`nes-icon github is-medium`} href={`https://github.com/juanmgart92`} isExternal={true} sx={{"textDecoration": "none", "_hover": {"color": "#EA5940 !important", "textDecoration": "none"}}}>
  {``}
</Link>
  <Link as={NextLink} className={`nes-icon youtube is-medium`} href={`https://www.youtube.com/@juanmgart/videos`} isExternal={true} sx={{"textDecoration": "none", "_hover": {"color": "#EA5940 !important", "textDecoration": "none"}}}>
  {``}
</Link>
  <Link as={NextLink} className={`nes-icon linkedin is-medium`} href={`https://www.linkedin.com/in/juanmagart`} isExternal={true} sx={{"textDecoration": "none", "_hover": {"color": "#EA5940 !important", "textDecoration": "none"}}}>
  {``}
</Link>
</HStack>
</VStack>
  <Center>
  <VStack spacing={`4em`} sx={{"width": "100%"}}>
  <VStack sx={{"alignItems": "center", "paddingX": "2em", "width": "100%", "maxWidth": "1000px", "paddingTop": "4em"}}>
  <Heading size={`lg`} sx={{"paddingBottom": "1em", "color": "#EA5940 !important", "fontFamily": "Press Start 2P"}}>
  {`Welcome to my page!`}
</Heading>
  <Flex sx={{"flexDirection": ["column", "column", "column", "row", "row"]}}>
  <ChakraImage alt={`Logo juanma`} src={`logojuan.png`} sx={{"width": "16em", "height": "16em", "marginRight": "2em"}}/>
  <VStack alignItems={`start`}>
  <Box className={`nes-balloon from-left is-dark`}>
  <Text>
  {`¡Hi Coders!`}
</Text>
  <Text>
  {`I´m Juan Manuel`}
</Text>
</Box>
  <Text as={`span`} sx={{"fontSize": "0.8em"}}>
  {`I am a dedicated software engineer with a track record of leading projects and crafting inventive solutions. My emphasis lies in enhancing operational efficiency and ensuring code quality for `}
  <Text as={`span`} sx={{"color": "#EA5940 !important", "fontSize": "1em"}}>
  {`outstanding outcomes`}
</Text>
  {`!`}
</Text>
  <Text as={`span`} sx={{"fontSize": "0.8em"}}>
  {`My website, built in Python using the REFLEX framework, aims to deliver an exceptional user experience by creating intuitive and efficient user interfaces.`}
</Text>
  <Link as={NextLink} href={`https://reflex.dev/`} isExternal={true} sx={{"color": "#D3D3D3", "paddingTop": "2em", "fontSize": "0.8em", "textDecoration": "none", "_hover": {"color": "#EA5940 !important", "textDecoration": "none"}}}>
  {`#REFLEX`}
</Link>
</VStack>
</Flex>
</VStack>
  <HStack alignItems={`center`} sx={{"alignItems": "center", "paddingX": "2em", "width": "100%", "maxWidth": "1000px", "paddingBottom": "2em"}}>
  <VStack alignItems={`start`} spacing={`0.8em`}>
  <Text sx={{"fontSize": "0.8em", "marginBottom": "0px !important"}}>
  {`© 2024 Juan Manuel Guerrero`}
</Text>
  <Link as={``} isExternal={true} sx={{"fontSize": "0.8em", "color": "#D3D3D3", "textDecoration": "none", "_hover": {"color": "#EA5940 !important", "textDecoration": "none"}}}>
  {`Creado con `}
  <Box className={`nes-icon is-small heart`}/>
  {` por Juanmgart`}
</Link>
</VStack>
  <Spacer/>
  <ChakraImage alt={`Logo juanma y simbolo coder`} className={`nes-avatar is-large`} src={`juanmgart.png`} sx={{"width": "4em", "height": "4em"}}/>
</HStack>
</VStack>
</Center>
</Box>
  <NextHead>
  <title>
  {`Juanma´s Reflex App`}
</title>
  <meta content={`Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
