import React, { useState, useEffect } from "react";
import "./styles.css";
import { Magic } from "magic-sdk";
import { TezosExtension } from "@magic-ext/tezos";

export default function App() {
  const [email, setEmail] = useState("");
  const [publicAddress, setPublicAddress] = useState("");
  const [destinationAddress, setDestinationAddress] = useState("");
  const [sendXTZAmount, setSendXTZAmount] = useState(0);
  const [contractoperationGroupID, setContractoperationGroupID] = useState("");
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [userMetadata, setUserMetadata] = useState({});
  const [
    transactionOperationGroupID,
    setTransactionOperationGroupID
  ] = useState("");
  const rpcUrl = "https://hangzhounet.api.tez.ie/";

  const magic = new Magic("pk_live_198606848E5E70FD", {
    extensions: {
      tezos: new TezosExtension({
        rpcUrl
      })
    }
  });

  useEffect(() => {
    magic.user.isLoggedIn().then(async (magicIsLoggedIn) => {
      setIsLoggedIn(magicIsLoggedIn);
      if (magicIsLoggedIn) {
        const publicAddress = await magic.tezos.getAccount();
        setPublicAddress(publicAddress);
        setUserMetadata(await magic.user.getMetadata());
      }
    });
  }, [isLoggedIn]);

  const login = async () => {
    await magic.auth.loginWithMagicLink({ email });
    setIsLoggedIn(true);
  };

  const logout = async () => {
    await magic.user.logout();
    setIsLoggedIn(false);
  };

  const handlerSendTransaction = async () => {
    const result = await magic.tezos.sendTransactionOperation(
      destinationAddress, // to
      parseInt(sendXTZAmount * 1000000), // amount
      15000, // fee
      "" // derivation path
    );

    console.log(result);

    const operationGroupID = result.operationGroupID.trim();

    setTransactionOperationGroupID(
      operationGroupID.substring(1, operationGroupID.length - 1)
    );
    console.log(`Injected operation group id ${operationGroupID}`);
  };

  const handleSendContractOrigination = async () => {
    const contract = `[
    {
       "prim":"parameter",
       "args":[ { "prim":"string" } ]
    },
    {
       "prim":"storage",
       "args":[ { "prim":"string" } ]
    },
    {
       "prim":"code",
       "args":[
          [  
             { "prim":"CAR" },
             { "prim":"NIL", "args":[ { "prim":"operation" } ] },
             { "prim":"PAIR" }
          ]
       ]
    }
 ]`;
    const storage = '{"string": "Sample"}';

    const params = {
      amount: 0,
      delegate: undefined,
      fee: 100000,
      derivationPath: "",
      storage_limit: 1000,
      gas_limit: 100000,
      code: contract,
      storage,
      codeFormat: "micheline"
    };

    const result = await magic.tezos.sendContractOriginationOperation(
      params.amount,
      params.delegate,
      params.fee,
      params.derivationPath,
      params.storage_limit,
      params.gas_limit,
      params.code,
      params.storage,
      params.codeFormat
    );

    const operationGroupID = result.operationGroupID.trim();

    setContractoperationGroupID(
      operationGroupID.substring(1, operationGroupID.length - 1)
    );
    console.log(
      `Injected operation group id ${result.operationGroupID}`,
      result
    );
  };

  return (
    <div className="App">
      {!isLoggedIn ? (
        <div className="container">
          <h1>Please sign up or login</h1>
          <input
            type="email"
            name="email"
            required="required"
            placeholder="Enter your email"
            onChange={(event) => {
              setEmail(event.target.value);
            }}
          />
          <button onClick={login}>Send</button>
        </div>
      ) : (
        <div>
          <div className="container">
            <h1>Current user: {userMetadata.email}</h1>
            <button onClick={logout}>Logout</button>
          </div>
          <div className="container">
            <h1>Tezos address</h1>
            <div className="info">
              <a
                href={`https://hangzhou2net.tzkt.io/${publicAddress}/operations/`}
                target="_blank"
              >
                {publicAddress}
              </a>
            </div>
          </div>
          <div className="container">
            <h1>Faucet</h1>
            <button>
              <a href="tg://resolve?domain=tezos_faucet_bot" target="_blank">
                Telegram Bot
              </a>
            </button>
          </div>
          <div className="container">
            <h1>Send Transaction</h1>
            {transactionOperationGroupID ? (
              <div>
                <div>Send transaction success</div>
                <div className="info">
                  <a
                    href={`https://hangzhou2net.tzkt.io/${transactionOperationGroupID}`}
                    target="_blank"
                  >
                    {transactionOperationGroupID}
                  </a>
                </div>
              </div>
            ) : (
              <div />
            )}
            <input
              type="text"
              name="destination"
              className="full-width"
              required="required"
              placeholder="Destination address"
              onChange={(event) => {
                setDestinationAddress(event.target.value);
              }}
            />
            <input
              type="text"
              name="amount"
              className="full-width"
              required="required"
              placeholder="Amount in XTZ"
              onChange={(event) => {
                setSendXTZAmount(event.target.value);
              }}
            />
            <button id="btn-send-txn" onClick={handlerSendTransaction}>
              Send Transaction
            </button>
          </div>
          <div className="container">
            <h1>Smart Contract</h1>
            <div className="info">
              <a
                href={`https://hangzhou2net.tzkt.io/${contractoperationGroupID}`}
                target="_blank"
              >
                {contractoperationGroupID}
              </a>
            </div>
            <button id="btn-deploy" onClick={handleSendContractOrigination}>
              Deploy Contract
            </button>
          </div>
        </div>
      )}
    </div>
  );
}