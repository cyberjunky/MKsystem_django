using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.IO;
using System.Net;
using System.Threading;
using System.Windows.Forms;

namespace btc_rich1
{
    public partial class Form1 : Form
    {
        private DoTenTraderManager atb_manager_;
        private Thread rate_thread_;
        private string current_broker_;
        private string current_timeframe_;

        private ColumnHeader colOpen;
        private ColumnHeader colHigh;
        private ColumnHeader colLow;
        private ColumnHeader colClose;
        private ColumnHeader colHighest;
        private ColumnHeader colLowest;

        private ColumnHeader colOpenDateTime;
        private ColumnHeader colSize;
        private ColumnHeader colType;
        private ColumnHeader colOpenPrice;
        private ColumnHeader colCurrentPrice;
        private ColumnHeader colPNL;

        private ColumnHeader colOrderDateTime;
        private ColumnHeader colOrderSize;
        private ColumnHeader colOrderType;
        private ColumnHeader colOrderPrice;
        private ColumnHeader colOrderCurrentPrice;
        private ColumnHeader colOrderOutStandingSize;

        private ColumnHeader colLogDateTime;
        private ColumnHeader colDescription;

        public Form1()
        {

            ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
            Directory.CreateDirectory("log");
            this.atb_manager_ = new DoTenTraderManager(this);
            this.atb_manager_.IsEnglish = false;
            this.InitializeComponent();
            if (Constants.Mode == "Free")
                this.Text = "BTC Machine Ex";
            //this.ChangeLanguage(false);
            this.InitTimeframes();
            this.InitQuoteList();
            this.RefereshBrokers();
            this.rate_thread_ = new Thread(new ThreadStart(this.MarketDataProcess));
            this.rate_thread_.IsBackground = true;
            this.rate_thread_.Start();
        }

       
        private void InitTimeframes()
        {
            //foreach (object timeFrame in Constants.TimeFrames)
            //    this.comboTimeFrame.Items.Add(timeFrame);
            //this.comboTimeFrame.SelectedIndex = 3;
            //this.current_timeframe_ = this.comboTimeFrame.Text;
            this.current_timeframe_ = "H1";
        }

        private void InitQuoteList()
        {
            string[] items = new string[6];
            for (int index = 0; index < 6; ++index)
                items[index] = "0";
            this.listQuote.Items.Add(new ListViewItem(items)
            {
                Name = "Quote"
            });
        }

        private void RefereshBrokers()
        {
            //this.comboBroker.Items.Clear();
            //foreach (KeyValuePair<string, BrokerInfo> broker in this.atb_manager_.BrokerList)
            //    this.comboBroker.Items.Add((object)broker.Key);
            //this.comboBroker.SelectedIndex = 0;
            this.RefreshBrokerInfo();
        }

        private void RefreshBrokerInfo()
        {
            //string str1 = this.comboBroker.SelectedItem.ToString();
            string str1 = "Bybit";
            string str2 = "";
            if (this.atb_manager_.BrokerList.ContainsKey(str1))
            {
                //this.textAPIKey.Text = this.atb_manager_.BrokerList[str1].APIKey;
                str2 = this.atb_manager_.BrokerList[str1].Symbols;
            }
            this.current_broker_ = str1;
            //this.comboSymbol.Items.Clear();
            //this.comboSymbol.Items.Add((object)str2);
            //this.comboSymbol.SelectedIndex = 0;
            //if (str1 == "Bitflyer")
            //{
            //    this.labelAutoCurrency.Text = "BTC";
            //    this.labelManualCurrency.Text = "BTC";
            //    this.textAutoLot.Text = "0.01";
            //    this.textLot.Text = "0.01";
            //}
            //else if (str1 == "ByBit")
            //{
            //    this.labelAutoCurrency.Text = "USD";
            //    this.labelManualCurrency.Text = "USD";
            //    this.textAutoLot.Text = "100";
            //    this.textLot.Text = "100";
            //}

            //this.labelAutoCurrency.Text = "USD";
            //this.labelManualCurrency.Text = "USD";
            this.textAutoLot.Text = "100";
            //this.textLot.Text = "100";

            this.atb_manager_.LoginBroker(str1);
            this.atb_manager_.CurrentBroker = str1;
            this.atb_manager_.InitOHLCData();
            this.UpdateEquity(0.0, 0.0);
            this.UpdateTickLabel(0.0, 0.0);
            this.UpdateQuoteList(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
            this.UpdatePositionList((List<Position>)null);
        }

        public void UpdateEquity(double equity, double balance)
        {
            this.SetLabelText(this.labelEquityValue, equity.ToString());
            this.SetLabelText(this.labelBalanceValue, balance.ToString());
        }

        public void UpdateTickLabel(double bid, double ask)
        {
            this.SetLabelText(this.labelBid, bid.ToString());
            this.SetLabelText(this.labelAsk, ask.ToString());
        }

        public void UpdateQuoteList(
          double open,
          double high,
          double low,
          double close,
          double highest,
          double lowest)
        {
            if (this.listQuote.InvokeRequired)
            {
                this.Invoke((Delegate)new SetQuoteListCallBack(this.UpdateQuoteList), (object)open, (object)high, (object)low, (object)close, (object)highest, (object)lowest);
            }
            else
            {
                this.listQuote.Items[0].SubItems[0].Text = open.ToString();
                this.listQuote.Items[0].SubItems[1].Text = high.ToString();
                this.listQuote.Items[0].SubItems[2].Text = low.ToString();
                this.listQuote.Items[0].SubItems[3].Text = close.ToString();
                this.listQuote.Items[0].SubItems[4].Text = highest.ToString();
                this.listQuote.Items[0].SubItems[5].Text = lowest.ToString();
            }
        }


        public void UpdatePositionList(List<Position> position_list)
        {
            if (this.listPositions.InvokeRequired)
            {
                this.Invoke((Delegate)new SetPositionListCallBack(this.UpdatePositionList), (object)position_list);
            }
            else
            {
                if (position_list == null)
                    return;
                if (position_list.Count == 0)
                {
                    this.listPositions.Items.Clear();
                }
                else
                {
                    bool flag = false;
                    if (this.listPositions.Items.Count == position_list.Count)
                    {
                        for (int index = 0; index < position_list.Count; ++index)
                        {
                            string str1 = position_list[index].OpenDateTime.ToString("yyyy/MM/dd HH:mm:ss");
                            string text = this.listPositions.Items[index].SubItems[0].Text;
                            double num = 0.0;
                            string str2;
                            if (this.listPositions.Items[index].SubItems[2].Name == "Buy")
                            {
                                str2 = this.atb_manager_.IsEnglish ? "Buy" : "買";
                                num = this.atb_manager_.CurrentTick(this.current_broker_).Bid;
                            }
                            else
                            {
                                str2 = this.atb_manager_.IsEnglish ? "Sell" : "売";
                                num = this.atb_manager_.CurrentTick(this.current_broker_).Ask;
                            }
                            this.listPositions.Items[index].SubItems[2].Text = str2;
                            this.listPositions.Items[index].SubItems[4].Text = num.ToString();
                            string str3 = text;
                            if (str1 != str3)
                                flag = true;
                        }
                    }
                    else
                        flag = true;
                    if (!flag)
                        return;
                    this.listPositions.Items.Clear();
                    foreach (Position position in position_list)
                        this.listPositions.Items.Add(new ListViewItem(new string[6]
                        {
              position.OpenDateTime.ToString("yyyy/MM/dd HH:mm:ss"),
              position.Volume.ToString(),
              position.Type != 1 ? (this.atb_manager_.IsEnglish ? "Sell" : "売") : (this.atb_manager_.IsEnglish ? "Buy" : "買"),
              position.OpenPrice.ToString(),
              "XXX",
              position.PnL.ToString()
                        })
                        {
                            SubItems = {
                [2] = {
                  Name = position.Type == 1 ? "Buy" : "Sell"
                }
              },
                            Name = position.PositionID
                        });
                }
            }
        }

        public void SetLabelText(Label label, string text)
        {
            if (label.InvokeRequired)
                this.Invoke((Delegate)new SetLabelTextCallBack(this.SetLabelText), 
                    (object)label, (object)text);
            else
                label.Text = text;
        }


        private void MarketDataProcess()
        {
            while (true)
            {
                this.atb_manager_.OnTick(this.current_broker_, this.current_timeframe_);
                Thread.Sleep(1200);
            }
        }

        public void ShowMessageBox()
        {
            if (this.atb_manager_.IsEnglish)
            {
                int num1 = (int)MessageBox.Show("Auto trade has stopped because of many errors.");
            }
            else
            {
                int num2 = (int)MessageBox.Show("多くのエラーが発生して自動取引が中断されました。");
            }
        }

        public void SetUserID(string user_id) => this.labelUserID.Text = user_id;

        public void StopAutoTrade()
        {
            this.SetControlVisible((Control)this.buttonStop, false);
            this.SetControlVisible((Control)this.buttonAutoTrade, true);
            this.EnableButtons(true);
            this.atb_manager_.IsLogicRunning = false;
        }

        private void EnableButtons(bool is_enable)
        {
            //this.SetControlEnabled((Control)this.comboBroker, is_enable);
            //this.SetControlEnabled((Control)this.btnSettings, is_enable);
            //this.SetControlEnabled((Control)this.comboSymbol, is_enable);
            //this.SetControlEnabled((Control)this.comboTimeFrame, is_enable);
            //this.SetControlEnabled((Control)this.textWatchHours, is_enable);
            this.SetControlEnabled((Control)this.textAutoLot, is_enable);
        }

        public void SetControlEnabled(Control control, bool value)
        {
            if (control.InvokeRequired)
                this.Invoke((Delegate)new SetConrolEnabledCallBack(this.SetControlEnabled), (object)control, (object)value);
            else
                control.Enabled = value;
        }

        public void SetControlVisible(Control control, bool value)
        {
            if (control.InvokeRequired)
                this.Invoke((Delegate)new SetConrolVisibleCallBack(this.SetControlVisible), (object)control, (object)value);
            else
                control.Visible = value;
        }

        public void AppendLog(string time, string message)
        {
            if (this.listLogs.InvokeRequired)
                this.Invoke((Delegate)new AppendLogListCallBack(this.AppendLog), (object)time, (object)message);
            else
                this.listLogs.Items.Insert(0, new ListViewItem(new string[2]
                {
          time,
          message
                }));
        }


        private delegate void SetQuoteListCallBack(
          double open,
          double high,
          double low,
          double close,
          double highest,
          double lowest);

        private delegate void SetLabelTextCallBack(Label label, string text);

        private delegate void SetPositionListCallBack(List<Position> positions);

        private delegate void AppendLogListCallBack(string time, string message);

        private delegate void SetConrolVisibleCallBack(Control control, bool is_visible);

        private delegate void SetConrolEnabledCallBack(Control control, bool is_enabled);

        private void aPI設定ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (new BrokerSettings(this.atb_manager_).ShowDialog() != DialogResult.OK)
                return;
            this.atb_manager_.SaveInformations("Broker.cfg");
            this.RefreshBrokerInfo();
        }

        private void long注文ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (!this.atb_manager_.IsAllowed)
            {
                int num1 = (int)MessageBox.Show(
                    this.atb_manager_.IsEnglish ? "Not registerd" : "登録されていないユーザーです。");
            }
            else
            {
                double result = 1.0;
                int num2 = (int)this.atb_manager_.SendOrder(
                    this.current_broker_, result, 0.0, true);
            }
        }

        private void short注文ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (!this.atb_manager_.IsAllowed)
            {
                int num1 = (int)MessageBox.Show(
                    this.atb_manager_.IsEnglish ? "Not registerd" : "登録されていないユーザーです。");
            }
            else
            {
                double result = 1.0;
                int num2 = (int)this.atb_manager_.SendOrder(
                    this.current_broker_, result, 0.0, false);
            }
        }
    }
}
