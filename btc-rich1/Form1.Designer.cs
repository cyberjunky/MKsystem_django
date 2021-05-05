using System.Windows.Forms;

namespace btc_rich1
{
    partial class Form1
    {
        /// <summary>
        /// 必要なデザイナー変数です。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 使用中のリソースをすべてクリーンアップします。
        /// </summary>
        /// <param name="disposing">マネージド リソースを破棄する場合は true を指定し、その他の場合は false を指定します。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows フォーム デザイナーで生成されたコード

        /// <summary>
        /// デザイナー サポートに必要なメソッドです。このメソッドの内容を
        /// コード エディターで変更しないでください。
        /// </summary>
        private void InitializeComponent()
        {
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.設定ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.aPI設定ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.手動操作ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.long注文ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.short注文ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.listQuote = new System.Windows.Forms.ListView();
            this.colOpen = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colHigh = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colLow = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colClose = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colHighest = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colLowest = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.label1 = new System.Windows.Forms.Label();
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.tabPage1 = new System.Windows.Forms.TabPage();
            this.listPositions = new System.Windows.Forms.ListView();
            this.colOpenDateTime = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colSize = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colType = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colOpenPrice = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colCurrentPrice = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colPNL = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.tabPage2 = new System.Windows.Forms.TabPage();
            this.listOrders = new System.Windows.Forms.ListView();
            this.colOrderDateTime = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colOrderSize = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colOrderType = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colOrderOutStandingSize = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colOrderPrice = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colOrderCurrentPrice = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.tabPage3 = new System.Windows.Forms.TabPage();
            this.listLogs = new System.Windows.Forms.ListView();
            this.colLogDateTime = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colDescription = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.textAutoLot = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.button1 = new System.Windows.Forms.Button();
            this.buttonAutoTrade = new System.Windows.Forms.Button();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.labelBalanceValue = new System.Windows.Forms.Label();
            this.labelEquityValue = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.labelBid = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.labelAsk = new System.Windows.Forms.Label();
            this.label10 = new System.Windows.Forms.Label();
            this.labelUserID = new System.Windows.Forms.Label();
            this.buttonStop = new System.Windows.Forms.Button();
            this.menuStrip1.SuspendLayout();
            this.tabControl1.SuspendLayout();
            this.tabPage1.SuspendLayout();
            this.tabPage2.SuspendLayout();
            this.tabPage3.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.設定ToolStripMenuItem,
            this.手動操作ToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(695, 24);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // 設定ToolStripMenuItem
            // 
            this.設定ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.aPI設定ToolStripMenuItem});
            this.設定ToolStripMenuItem.Name = "設定ToolStripMenuItem";
            this.設定ToolStripMenuItem.Size = new System.Drawing.Size(43, 20);
            this.設定ToolStripMenuItem.Text = "設定";
            // 
            // aPI設定ToolStripMenuItem
            // 
            this.aPI設定ToolStripMenuItem.Name = "aPI設定ToolStripMenuItem";
            this.aPI設定ToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.aPI設定ToolStripMenuItem.Text = "API設定";
            this.aPI設定ToolStripMenuItem.Click += new System.EventHandler(this.aPI設定ToolStripMenuItem_Click);
            // 
            // 手動操作ToolStripMenuItem
            // 
            this.手動操作ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.long注文ToolStripMenuItem,
            this.short注文ToolStripMenuItem});
            this.手動操作ToolStripMenuItem.Name = "手動操作ToolStripMenuItem";
            this.手動操作ToolStripMenuItem.Size = new System.Drawing.Size(67, 20);
            this.手動操作ToolStripMenuItem.Text = "手動操作";
            // 
            // long注文ToolStripMenuItem
            // 
            this.long注文ToolStripMenuItem.Name = "long注文ToolStripMenuItem";
            this.long注文ToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.long注文ToolStripMenuItem.Text = "Long注文";
            this.long注文ToolStripMenuItem.Click += new System.EventHandler(this.long注文ToolStripMenuItem_Click);
            // 
            // short注文ToolStripMenuItem
            // 
            this.short注文ToolStripMenuItem.Name = "short注文ToolStripMenuItem";
            this.short注文ToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.short注文ToolStripMenuItem.Text = "Short注文";
            this.short注文ToolStripMenuItem.Click += new System.EventHandler(this.short注文ToolStripMenuItem_Click);
            // 
            // listQuote
            // 
            this.listQuote.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.colOpen,
            this.colHigh,
            this.colLow,
            this.colClose,
            this.colHighest,
            this.colLowest});
            this.listQuote.Font = new System.Drawing.Font("Meiryo UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.listQuote.HideSelection = false;
            this.listQuote.Location = new System.Drawing.Point(15, 58);
            this.listQuote.Name = "listQuote";
            this.listQuote.Size = new System.Drawing.Size(666, 51);
            this.listQuote.TabIndex = 1;
            this.listQuote.UseCompatibleStateImageBehavior = false;
            this.listQuote.View = System.Windows.Forms.View.Details;
            // 
            // colOpen
            // 
            this.colOpen.Text = "Open";
            this.colOpen.Width = 110;
            // 
            // colHigh
            // 
            this.colHigh.Text = "High";
            this.colHigh.Width = 110;
            // 
            // colLow
            // 
            this.colLow.Text = "Low";
            this.colLow.Width = 110;
            // 
            // colClose
            // 
            this.colClose.Text = "Close";
            this.colClose.Width = 110;
            // 
            // colHighest
            // 
            this.colHighest.Text = "Highest";
            this.colHighest.Width = 110;
            // 
            // colLowest
            // 
            this.colLowest.Text = "Lowest";
            this.colLowest.Width = 110;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Meiryo UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.label1.Location = new System.Drawing.Point(12, 40);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(55, 15);
            this.label1.TabIndex = 2;
            this.label1.Text = "価格情報";
            // 
            // tabControl1
            // 
            this.tabControl1.Controls.Add(this.tabPage1);
            this.tabControl1.Controls.Add(this.tabPage2);
            this.tabControl1.Controls.Add(this.tabPage3);
            this.tabControl1.Font = new System.Drawing.Font("Meiryo UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.tabControl1.Location = new System.Drawing.Point(15, 123);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(666, 122);
            this.tabControl1.TabIndex = 3;
            // 
            // tabPage1
            // 
            this.tabPage1.Controls.Add(this.listPositions);
            this.tabPage1.Location = new System.Drawing.Point(4, 24);
            this.tabPage1.Name = "tabPage1";
            this.tabPage1.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage1.Size = new System.Drawing.Size(658, 94);
            this.tabPage1.TabIndex = 0;
            this.tabPage1.Text = "ポジション";
            this.tabPage1.UseVisualStyleBackColor = true;
            // 
            // listPositions
            // 
            this.listPositions.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.colOpenDateTime,
            this.colSize,
            this.colType,
            this.colOpenPrice,
            this.colCurrentPrice,
            this.colPNL});
            this.listPositions.HideSelection = false;
            this.listPositions.Location = new System.Drawing.Point(0, 0);
            this.listPositions.Name = "listPositions";
            this.listPositions.Size = new System.Drawing.Size(658, 94);
            this.listPositions.TabIndex = 6;
            this.listPositions.UseCompatibleStateImageBehavior = false;
            this.listPositions.View = System.Windows.Forms.View.Details;
            // 
            // colOpenDateTime
            // 
            this.colOpenDateTime.Text = "日付時間";
            this.colOpenDateTime.Width = 120;
            // 
            // colSize
            // 
            this.colSize.Text = "取引数量";
            this.colSize.Width = 90;
            // 
            // colType
            // 
            this.colType.Text = "買/売";
            // 
            // colOpenPrice
            // 
            this.colOpenPrice.Text = "参入価格";
            this.colOpenPrice.Width = 110;
            // 
            // colCurrentPrice
            // 
            this.colCurrentPrice.Text = "価格";
            this.colCurrentPrice.Width = 110;
            // 
            // colPNL
            // 
            this.colPNL.Text = "利益";
            this.colPNL.Width = 110;
            // 
            // tabPage2
            // 
            this.tabPage2.Controls.Add(this.listOrders);
            this.tabPage2.Location = new System.Drawing.Point(4, 24);
            this.tabPage2.Name = "tabPage2";
            this.tabPage2.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage2.Size = new System.Drawing.Size(658, 94);
            this.tabPage2.TabIndex = 1;
            this.tabPage2.Text = "ペンディング";
            this.tabPage2.UseVisualStyleBackColor = true;
            // 
            // listOrders
            // 
            this.listOrders.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.colOrderDateTime,
            this.colOrderSize,
            this.colOrderType,
            this.colOrderOutStandingSize,
            this.colOrderPrice,
            this.colOrderCurrentPrice});
            this.listOrders.HideSelection = false;
            this.listOrders.Location = new System.Drawing.Point(0, 0);
            this.listOrders.Name = "listOrders";
            this.listOrders.Size = new System.Drawing.Size(658, 94);
            this.listOrders.TabIndex = 0;
            this.listOrders.UseCompatibleStateImageBehavior = false;
            this.listOrders.View = System.Windows.Forms.View.Details;
            // 
            // colOrderDateTime
            // 
            this.colOrderDateTime.Text = "日付時間";
            this.colOrderDateTime.Width = 120;
            // 
            // colOrderSize
            // 
            this.colOrderSize.Text = "取引数量";
            this.colOrderSize.Width = 100;
            // 
            // colOrderType
            // 
            this.colOrderType.Text = "買/売";
            this.colOrderType.Width = 80;
            // 
            // colOrderOutStandingSize
            // 
            this.colOrderOutStandingSize.Text = "未締結数量";
            this.colOrderOutStandingSize.Width = 100;
            // 
            // colOrderPrice
            // 
            this.colOrderPrice.Text = "注文価格";
            this.colOrderPrice.Width = 110;
            // 
            // colOrderCurrentPrice
            // 
            this.colOrderCurrentPrice.Text = "価格";
            this.colOrderCurrentPrice.Width = 110;
            // 
            // tabPage3
            // 
            this.tabPage3.Controls.Add(this.listLogs);
            this.tabPage3.Location = new System.Drawing.Point(4, 24);
            this.tabPage3.Name = "tabPage3";
            this.tabPage3.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage3.Size = new System.Drawing.Size(658, 94);
            this.tabPage3.TabIndex = 2;
            this.tabPage3.Text = "ログ";
            this.tabPage3.UseVisualStyleBackColor = true;
            // 
            // listLogs
            // 
            this.listLogs.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.colLogDateTime,
            this.colDescription});
            this.listLogs.HideSelection = false;
            this.listLogs.Location = new System.Drawing.Point(0, 0);
            this.listLogs.Name = "listLogs";
            this.listLogs.Size = new System.Drawing.Size(658, 94);
            this.listLogs.TabIndex = 1;
            this.listLogs.UseCompatibleStateImageBehavior = false;
            this.listLogs.View = System.Windows.Forms.View.Details;
            // 
            // colLogDateTime
            // 
            this.colLogDateTime.Text = "日付時間";
            this.colLogDateTime.Width = 120;
            // 
            // colDescription
            // 
            this.colDescription.Text = "説明";
            this.colDescription.Width = 500;
            // 
            // textAutoLot
            // 
            this.textAutoLot.Font = new System.Drawing.Font("Meiryo UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.textAutoLot.Location = new System.Drawing.Point(538, 257);
            this.textAutoLot.Name = "textAutoLot";
            this.textAutoLot.Size = new System.Drawing.Size(100, 23);
            this.textAutoLot.TabIndex = 4;
            this.textAutoLot.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Meiryo UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.label2.Location = new System.Drawing.Point(501, 265);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(31, 15);
            this.label2.TabIndex = 2;
            this.label2.Text = "数量";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Meiryo UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.label3.Location = new System.Drawing.Point(644, 265);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(33, 15);
            this.label3.TabIndex = 2;
            this.label3.Text = "USD";
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("Meiryo UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.button1.Location = new System.Drawing.Point(474, 296);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(86, 37);
            this.button1.TabIndex = 5;
            this.button1.Text = "一括決済";
            this.button1.UseVisualStyleBackColor = true;
            // 
            // buttonAutoTrade
            // 
            this.buttonAutoTrade.Font = new System.Drawing.Font("Meiryo UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.buttonAutoTrade.Location = new System.Drawing.Point(591, 296);
            this.buttonAutoTrade.Name = "buttonAutoTrade";
            this.buttonAutoTrade.Size = new System.Drawing.Size(86, 37);
            this.buttonAutoTrade.TabIndex = 5;
            this.buttonAutoTrade.Text = "スタート";
            this.buttonAutoTrade.UseVisualStyleBackColor = true;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Meiryo UI", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.label4.Location = new System.Drawing.Point(55, 276);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(34, 17);
            this.label4.TabIndex = 2;
            this.label4.Text = "数量";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("Meiryo UI", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.label5.Location = new System.Drawing.Point(37, 298);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(53, 17);
            this.label5.TabIndex = 2;
            this.label5.Text = "エクイティ";
            // 
            // labelBalanceValue
            // 
            this.labelBalanceValue.AutoSize = true;
            this.labelBalanceValue.Font = new System.Drawing.Font("Meiryo UI", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.labelBalanceValue.Location = new System.Drawing.Point(112, 276);
            this.labelBalanceValue.Name = "labelBalanceValue";
            this.labelBalanceValue.Size = new System.Drawing.Size(85, 17);
            this.labelBalanceValue.TabIndex = 2;
            this.labelBalanceValue.Text = "0.00000000";
            this.labelBalanceValue.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // labelEquityValue
            // 
            this.labelEquityValue.AutoSize = true;
            this.labelEquityValue.Font = new System.Drawing.Font("Meiryo UI", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.labelEquityValue.ImageAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.labelEquityValue.Location = new System.Drawing.Point(112, 298);
            this.labelEquityValue.Name = "labelEquityValue";
            this.labelEquityValue.Size = new System.Drawing.Size(85, 17);
            this.labelEquityValue.TabIndex = 2;
            this.labelEquityValue.Text = "0.00000000";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Font = new System.Drawing.Font("Meiryo UI", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.label8.Location = new System.Drawing.Point(194, 276);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(34, 17);
            this.label8.TabIndex = 2;
            this.label8.Text = "BTC";
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Font = new System.Drawing.Font("Meiryo UI", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.label9.Location = new System.Drawing.Point(194, 298);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(34, 17);
            this.label9.TabIndex = 2;
            this.label9.Text = "BTC";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Font = new System.Drawing.Font("Meiryo UI", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.label6.Location = new System.Drawing.Point(283, 276);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(28, 17);
            this.label6.TabIndex = 2;
            this.label6.Text = "Bid";
            // 
            // labelBid
            // 
            this.labelBid.AutoSize = true;
            this.labelBid.Font = new System.Drawing.Font("Meiryo UI", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.labelBid.Location = new System.Drawing.Point(340, 276);
            this.labelBid.Name = "labelBid";
            this.labelBid.Size = new System.Drawing.Size(69, 17);
            this.labelBid.TabIndex = 2;
            this.labelBid.Text = "100000.0";
            this.labelBid.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Font = new System.Drawing.Font("Meiryo UI", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.label7.Location = new System.Drawing.Point(283, 298);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(30, 17);
            this.label7.TabIndex = 2;
            this.label7.Text = "Ask";
            // 
            // labelAsk
            // 
            this.labelAsk.AutoSize = true;
            this.labelAsk.Font = new System.Drawing.Font("Meiryo UI", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.labelAsk.Location = new System.Drawing.Point(340, 298);
            this.labelAsk.Name = "labelAsk";
            this.labelAsk.Size = new System.Drawing.Size(69, 17);
            this.labelAsk.TabIndex = 2;
            this.labelAsk.Text = "100000.0";
            this.labelAsk.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Font = new System.Drawing.Font("Meiryo UI", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.label10.Location = new System.Drawing.Point(55, 252);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(32, 17);
            this.label10.TabIndex = 2;
            this.label10.Text = "UID";
            // 
            // labelUserID
            // 
            this.labelUserID.AutoSize = true;
            this.labelUserID.Font = new System.Drawing.Font("Meiryo UI", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.labelUserID.Location = new System.Drawing.Point(112, 252);
            this.labelUserID.Name = "labelUserID";
            this.labelUserID.Size = new System.Drawing.Size(53, 17);
            this.labelUserID.TabIndex = 2;
            this.labelUserID.Text = "XXXXX";
            this.labelUserID.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // buttonStop
            // 
            this.buttonStop.Font = new System.Drawing.Font("Meiryo UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.buttonStop.Location = new System.Drawing.Point(591, 296);
            this.buttonStop.Name = "buttonStop";
            this.buttonStop.Size = new System.Drawing.Size(86, 37);
            this.buttonStop.TabIndex = 6;
            this.buttonStop.Text = "ストップ";
            this.buttonStop.UseVisualStyleBackColor = true;
            this.buttonStop.Visible = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(695, 345);
            this.Controls.Add(this.buttonStop);
            this.Controls.Add(this.buttonAutoTrade);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.textAutoLot);
            this.Controls.Add(this.tabControl1);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.labelEquityValue);
            this.Controls.Add(this.labelAsk);
            this.Controls.Add(this.labelBid);
            this.Controls.Add(this.labelUserID);
            this.Controls.Add(this.labelBalanceValue);
            this.Controls.Add(this.label9);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.label10);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.listQuote);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "Form1";
            this.Text = "btc-rich1";
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.tabControl1.ResumeLayout(false);
            this.tabPage1.ResumeLayout(false);
            this.tabPage2.ResumeLayout(false);
            this.tabPage3.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem 設定ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem aPI設定ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 手動操作ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem long注文ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem short注文ToolStripMenuItem;
        private System.Windows.Forms.ListView listQuote;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage tabPage1;
        private System.Windows.Forms.TabPage tabPage2;
        private System.Windows.Forms.TabPage tabPage3;
        private System.Windows.Forms.TextBox textAutoLot;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button buttonAutoTrade;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label labelBalanceValue;
        private System.Windows.Forms.Label labelEquityValue;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label labelBid;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label labelAsk;
        private System.Windows.Forms.ListView listPositions;
        private ListView listOrders;
        private ListView listLogs;
        private Label label10;
        private Label labelUserID;
        private Button buttonStop;
    }
}

